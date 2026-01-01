## 1. Implementation
- [x] 1.1 Update `backend/main.py` to accept optional `resolution` and `video_format` parameters in the download endpoint.
- [x] 1.2 Implement logic in `backend/main.py` to map resolution/format choices to `yt-dlp` format strings.
- [x] 1.3 Update `frontend/app.py` to include `st.selectbox` for Resolution and Format.
- [x] 1.4 Update `frontend/app.py` to pass the selected values in the API request.
- [x] 1.5 Verify downloads work with specific resolution limits (e.g., 480p).
- [x] 1.6 Verify downloads work with specific formats (e.g., webm).
