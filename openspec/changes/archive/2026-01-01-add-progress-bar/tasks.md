## 1. Implementation
- [x] 1.1 Define the progress tracking data structure in `backend/main.py` (e.g., a global dictionary for `task_id` -> `progress`).
- [x] 1.2 Create a `POST /api/download/start` endpoint that accepts the URL, starts the download in a background thread, and returns a `task_id`.
- [x] 1.3 Implement the `yt-dlp` progress hook to update the global progress dictionary.
- [x] 1.4 Create a `GET /api/download/progress/{task_id}` endpoint to return status (pending, downloading, completed, error) and percentage.
- [x] 1.5 Create a `GET /api/download/file/{task_id}` endpoint to serve the downloaded file.
- [x] 1.6 Update `frontend/app.py` to use the new flow: start download -> loop/poll progress -> show download button.
- [x] 1.7 Verify the progress bar works for a sample video.
