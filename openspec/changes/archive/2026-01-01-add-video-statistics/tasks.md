## 1. Backend Implementation
- [x] 1.1 Implement `/api/info` endpoint in `backend/main.py` that uses `yt_dlp.extract_info(download=False)`.
- [x] 1.2 Ensure the endpoint returns Title, Uploader, Views, Duration, and Thumbnail URL.
- [x] 1.3 Add error handling for invalid URLs or extraction failures.

## 2. Frontend Implementation
- [x] 2.1 Add a mechanism (e.g., button or auto-fetch) in `frontend/app.py` to trigger the info fetch.
- [x] 2.2 Display the returned statistics (Title, Channel, Views, Duration) and Thumbnail in the UI.
- [x] 2.3 Ensure statistics are shown before or alongside the download controls.

## 3. Validation
- [x] 3.1 Verify that correct metadata is displayed for valid YouTube URLs.
- [x] 3.2 Verify that invalid URLs display an appropriate error message without crashing.
