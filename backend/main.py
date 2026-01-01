import os
import uuid
from typing import Optional, Dict, Any, cast
from fastapi import FastAPI, HTTPException, BackgroundTasks, Query
from fastapi.responses import FileResponse
import yt_dlp

app = FastAPI()

RESOLUTION_MAP = {
    "Best": "best",
    "1080p": "bestvideo[height<=1080]",
    "720p": "bestvideo[height<=720]",
    "480p": "bestvideo[height<=480]",
    "360p": "bestvideo[height<=360]",
}

VIDEO_FORMAT_MAP = {
    "mp4": "",
    "mkv": "[ext=mkv]",
    "webm": "[ext=webm]",
}

AUDIO_QUALITY_MAP = {
    "Best": "best",
    "320kbps": "320",
    "256kbps": "256",
    "192kbps": "192",
    "128kbps": "128",
}

DOWNLOAD_DIR = "downloads"
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

# Global dictionary to track download tasks
# Structure: task_id -> {"status": str, "progress": float, "filename": str, "error": str}
tasks: Dict[str, Dict[str, Any]] = {}


def cleanup_file(path: str):
    """Removes the file after it has been sent."""
    try:
        if os.path.exists(path):
            os.remove(path)
    except Exception as e:
        print(f"Error cleaning up {path}: {e}")


def progress_hook(d, task_id):
    if d["status"] == "downloading":
        try:
            p = d.get("_percent_str", "0%").replace("%", "")
            tasks[task_id]["progress"] = float(p)
            tasks[task_id]["status"] = "downloading"
        except ValueError:
            pass
    elif d["status"] == "finished":
        tasks[task_id]["progress"] = 100.0
        tasks[task_id]["status"] = "processing"


def run_download(
    task_id: str,
    url: str,
    resolution: Optional[str],
    video_format: Optional[str],
    media_type: str = "video",
    audio_quality: str = "Best",
):
    try:
        tasks[task_id]["status"] = "starting"
        output_template = f"{DOWNLOAD_DIR}/{task_id}.%(ext)s"

        def hook(d):
            progress_hook(d, task_id)

        ydl_opts: Dict[str, Any] = {
            "outtmpl": output_template,
            "noplaylist": True,
            "progress_hooks": [hook],
        }

        if media_type == "audio":
            ydl_opts["format"] = "bestaudio/best"
            ydl_opts["postprocessors"] = [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": AUDIO_QUALITY_MAP.get(audio_quality, "best"),
                },
                {
                    "key": "FFmpegMetadata",
                },
            ]
        else:
            base_format = "best"
            if resolution and resolution in RESOLUTION_MAP:
                base_format = RESOLUTION_MAP[resolution]

            format_ext = ""
            if video_format and video_format in VIDEO_FORMAT_MAP:
                format_ext = VIDEO_FORMAT_MAP[video_format]

            format_str = f"{base_format}{format_ext}+bestaudio/best"

            merge_format = "mp4"
            if video_format in ["mp4", "mkv", "webm"]:
                merge_format = video_format

            ydl_opts["format"] = format_str
            ydl_opts["merge_output_format"] = merge_format

        with yt_dlp.YoutubeDL(cast(Any, ydl_opts)) as ydl:
            info = ydl.extract_info(url, download=True)
            original_filename = ydl.prepare_filename(info)

            # For audio downloads, the actual file will be converted to .mp3 after post-processing
            if media_type == "audio":
                # Change extension to .mp3
                base_name = os.path.splitext(original_filename)[0]
                filename = base_name + ".mp3"
            else:
                filename = original_filename

        tasks[task_id]["filename"] = filename
        tasks[task_id]["status"] = "completed"
        tasks[task_id]["progress"] = 100.0

    except Exception as e:
        tasks[task_id]["status"] = "error"
        tasks[task_id]["error"] = str(e)


@app.post("/api/download/start")
async def start_download(
    background_tasks: BackgroundTasks,
    url: str = Query(...),
    resolution: Optional[str] = Query(None),
    video_format: Optional[str] = Query(None),
    media_type: str = Query("video"),
    audio_quality: str = Query("Best"),
):
    task_id = str(uuid.uuid4())
    tasks[task_id] = {"status": "pending", "progress": 0.0, "filename": None, "error": None}

    background_tasks.add_task(
        run_download, task_id, url, resolution, video_format, media_type, audio_quality
    )

    return {"task_id": task_id}


@app.get("/api/download/progress/{task_id}")
async def get_progress(task_id: str):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]


@app.get("/api/download/file/{task_id}")
async def get_file(task_id: str, background_tasks: BackgroundTasks):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    task = tasks[task_id]
    if (
        task["status"] != "completed"
        or not task["filename"]
        or not os.path.exists(task["filename"])
    ):
        raise HTTPException(status_code=400, detail="File not ready or missing")

    filename = task["filename"]

    # Determine media type
    media_type = "video/mp4"
    if filename.endswith(".webm"):
        media_type = "video/webm"
    elif filename.endswith(".mkv"):
        media_type = "video/x-matroska"
    elif filename.endswith(".mp3"):
        media_type = "audio/mpeg"

    background_tasks.add_task(cleanup_file, filename)

    return FileResponse(
        path=filename,
        filename=os.path.basename(filename),
        media_type=media_type,
    )


@app.get("/api/info")
async def get_video_info(url: str = Query(...)):
    try:
        ydl_opts: Dict[str, Any] = {
            "noplaylist": True,
        }
        with yt_dlp.YoutubeDL(cast(Any, ydl_opts)) as ydl:
            info = ydl.extract_info(url, download=False)
            return {
                "title": info.get("title"),
                "uploader": info.get("uploader"),
                "views": info.get("view_count"),
                "duration": info.get("duration"),
                "thumbnail": info.get("thumbnail"),
            }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to extract video info: {str(e)}")


@app.get("/health")
def health_check():
    return {"status": "ok"}
