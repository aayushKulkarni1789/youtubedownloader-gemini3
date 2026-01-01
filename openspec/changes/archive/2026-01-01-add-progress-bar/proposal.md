# Change: Add Progress Bar for Video Downloads

## Why
Currently, when a user clicks "Download Video", the application appears to hang or just shows a generic spinner while the backend downloads the video from YouTube. This provides poor feedback, especially for large videos. Users need to see real-time progress to know the application is working and how long it will take.

## What Changes
- **Backend:**
  - Refactor the `/download` endpoint to be asynchronous/background-task based (or add a new flow).
  - Introduce a "start download" endpoint that initiates the process and returns a Task ID.
  - Introduce a "progress" endpoint that returns the current percentage and status for a Task ID.
  - Introduce a "get file" endpoint to retrieve the final file.
  - Implement a `yt-dlp` progress hook to update the task status.
- **Frontend:**
  - Update the UI to start the download, then poll the progress endpoint.
  - Display a `st.progress` bar updated with the polled value.
  - Upon completion, show the download button for the final file.

## Impact
- **Affected specs:** `video-download`
- **Affected code:** `backend/main.py`, `frontend/app.py`
- **Dependencies:** No new dependencies, but significantly changes the interaction model between frontend and backend.
