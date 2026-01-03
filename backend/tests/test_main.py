import os
import sys
import pytest
from unittest.mock import MagicMock, patch
from fastapi.testclient import TestClient

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app, tasks

client = TestClient(app)


@pytest.fixture
def mock_yt_dlp():
    with patch("main.yt_dlp.YoutubeDL") as mock:
        yield mock


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_get_video_info(mock_yt_dlp):
    mock_instance = mock_yt_dlp.return_value.__enter__.return_value
    mock_instance.extract_info.return_value = {
        "title": "Test Video",
        "uploader": "Test Uploader",
        "view_count": 1000,
        "duration": 60,
        "thumbnail": "http://example.com/thumb.jpg",
    }

    response = client.get("/api/info?url=http://youtube.com/watch?v=123")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Video"
    assert data["uploader"] == "Test Uploader"


def test_download_flow_integration(mock_yt_dlp):
    mock_instance = mock_yt_dlp.return_value.__enter__.return_value
    mock_instance.extract_info.return_value = {
        "id": "video_id",
        "title": "Test Video",
        "ext": "mp4",
    }
    mock_instance.prepare_filename.return_value = "downloads/test_task.mp4"

    response = client.post("/api/download/start?url=http://youtube.com/watch?v=123")
    assert response.status_code == 200
    data = response.json()
    assert "task_id" in data
    task_id = data["task_id"]

    assert task_id in tasks

    tasks[task_id]["status"] = "completed"
    tasks[task_id]["filename"] = "downloads/test_task.mp4"
    tasks[task_id]["progress"] = 100.0

    response = client.get(f"/api/download/progress/{task_id}")
    assert response.status_code == 200
    progress_data = response.json()
    assert progress_data["status"] == "completed"
    assert progress_data["progress"] == 100.0

    with patch("os.path.exists", return_value=True):
        with patch("main.FileResponse") as mock_file_response:
            with patch("os.remove"):
                response = client.get(f"/api/download/file/{task_id}")
                assert response.status_code == 200
