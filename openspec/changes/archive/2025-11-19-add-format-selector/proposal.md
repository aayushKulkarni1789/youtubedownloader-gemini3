# Change: Add Format and Resolution Selector

## Why
Users currently have no control over the quality or file format of the downloaded video; the system defaults to "best" and "mp4". Users may want lower resolutions to save space or specific formats (e.g., webm, mkv) for compatibility reasons.

## What Changes
- **Frontend:**
  - Add a "Resolution" dropdown (options: Best, 1080p, 720p, 480p, 360p).
  - Add a "Format" dropdown (options: mp4, mkv, webm).
  - Pass these selections to the backend download endpoint.
- **Backend:**
  - Update the download endpoint to accept `resolution` and `format` parameters.
  - Dynamically construct `yt-dlp` options based on these parameters (e.g., using `bestvideo[height<=1080]+bestaudio/best` logic).

## Impact
- **Affected specs:** `video-download`
- **Affected code:** `frontend/app.py`, `backend/main.py`
- **Dependencies:** None.


## Status
Completed on 2025-11-19
