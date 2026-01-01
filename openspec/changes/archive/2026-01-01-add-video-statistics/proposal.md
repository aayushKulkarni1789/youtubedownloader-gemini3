# Change: Add Video Statistics

## Why
Users currently download videos blindly without verifying if the URL corresponds to the correct video or knowing details like duration and popularity. Adding video statistics improves confidence and user experience.

## What Changes
- Add a new backend endpoint to retrieve video metadata (title, views, duration, etc.) using `yt-dlp` without downloading the file.
- Update the frontend to display these statistics after the user provides a URL.
- Display metadata such as Title, Channel/Uploader, View Count, Duration, and Thumbnail.

## Impact
- **Affected specs:** `video-metadata` (new capability)
- **Affected code:**
    - `backend/main.py`: New `/api/info` endpoint.
    - `frontend/app.py`: UI update to fetch and display stats.
