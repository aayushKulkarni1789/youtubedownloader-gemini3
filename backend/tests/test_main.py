import pytest
from backend.main import RESOLUTION_MAP, VIDEO_FORMAT_MAP, app
from fastapi.testclient import TestClient


def test_resolution_map():
    assert RESOLUTION_MAP["Best"] == "best"
    assert RESOLUTION_MAP["1080p"] == "bestvideo[height<=1080]"
    assert RESOLUTION_MAP["720p"] == "bestvideo[height<=720]"
    assert RESOLUTION_MAP["480p"] == "bestvideo[height<=480]"
    assert RESOLUTION_MAP["360p"] == "bestvideo[height<=360]"


def test_video_format_map():
    assert VIDEO_FORMAT_MAP["mp4"] == ""
    assert VIDEO_FORMAT_MAP["mkv"] == "[ext=mkv]"
    assert VIDEO_FORMAT_MAP["webm"] == "[ext=webm]"


@pytest.mark.parametrize(
    "resolution,expected_base",
    [
        ("Best", "best"),
        ("1080p", "bestvideo[height<=1080]"),
        ("720p", "bestvideo[height<=720]"),
        ("480p", "bestvideo[height<=480]"),
        ("360p", "bestvideo[height<=360]"),
    ],
)
@pytest.mark.parametrize(
    "video_format,expected_ext",
    [
        ("mp4", ""),
        ("mkv", "[ext=mkv]"),
        ("webm", "[ext=webm]"),
    ],
)
def test_format_string_assembly(resolution, expected_base, video_format, expected_ext):
    format_str = f"{expected_base}{expected_ext}+bestaudio/best"
    # Simulate the logic
    base_format = RESOLUTION_MAP.get(resolution, "best")
    format_ext = VIDEO_FORMAT_MAP.get(video_format, "")
    assembled_format_str = f"{base_format}{format_ext}+bestaudio/best"
    assert assembled_format_str == format_str


def test_ydl_opts_assembly():
    # Test for a specific case, e.g., 1080p mp4
    resolution = "1080p"
    video_format = "mp4"
    base_format = RESOLUTION_MAP[resolution]
    format_ext = VIDEO_FORMAT_MAP[video_format]
    format_str = f"{base_format}{format_ext}+bestaudio/best"
    merge_format = video_format

    ydl_opts = {
        "format": format_str,
        "outtmpl": "test.%(ext)s",
        "noplaylist": True,
        "merge_output_format": merge_format,
    }

    expected_opts = {
        "format": "bestvideo[height<=1080]+bestaudio/best",
        "outtmpl": "test.%(ext)s",
        "noplaylist": True,
        "merge_output_format": "mp4",
    }

    assert ydl_opts == expected_opts


def test_invalid_resolution_defaults():
    resolution = "invalid"
    base_format = RESOLUTION_MAP.get(resolution, "best")
    assert base_format == "best"


def test_invalid_format_defaults():
    video_format = "invalid"
    format_ext = VIDEO_FORMAT_MAP.get(video_format, "")
    assert format_ext == ""


def test_download_integration(mocker):
    client = TestClient(app)

    # Mock yt_dlp.YoutubeDL
    mock_ydl_class = mocker.patch("backend.main.yt_dlp.YoutubeDL")
    mock_ydl = mock_ydl_class.return_value.__enter__.return_value
    mock_ydl.extract_info.return_value = {"title": "Test Video"}
    mock_ydl.prepare_filename.return_value = "downloads/test-id.webm"

    # Mock os.path.exists to return True
    mocker.patch("backend.main.os.path.exists", return_value=True)

    # Mock uuid.uuid4
    mock_uuid = mocker.patch("backend.main.uuid.uuid4")
    mock_uuid.return_value = "test-id"

    response = client.post(
        "/download",
        params={
            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "resolution": "720p",
            "video_format": "webm",
        },
    )

    assert response.status_code == 200
    assert response.headers["content-type"] == "video/webm"
    assert "test-id.webm" in response.headers.get("content-disposition", "")

    # Verify yt_dlp was called with correct options
    expected_ydl_opts = {
        "format": "bestvideo[height<=720][ext=webm]+bestaudio/best",
        "outtmpl": "downloads/test-id.%(ext)s",
        "noplaylist": True,
        "merge_output_format": "webm",
    }
    mock_ydl_class.assert_called_once_with(expected_ydl_opts)
    mock_ydl.extract_info.assert_called_once_with(
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ", download=True
    )
