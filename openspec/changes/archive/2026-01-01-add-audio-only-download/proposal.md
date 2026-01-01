# Change: Add Audio-Only Download Support

## Why
Users currently can only download videos as complete media files, which is inefficient when they only need the audio track (e.g., podcasts, music, audio lectures). Downloading full videos wastes bandwidth and storage space. Adding audio-only download with MP3 support provides users with a more efficient option for audio content.

## What Changes
- **Backend:**
  - Add `media_type` parameter to distinguish between video and audio downloads
  - Add `audio_quality` parameter with options: Best, 320kbps, 256kbps, 192kbps, 128kbps
  - Implement audio-only download path using `bestaudio/best` format
  - Add FFmpeg post-processor to convert to MP3 with selected bitrate
  - Add FFmpeg metadata post-processor to embed title, artist, and uploader info
  - Update `/api/download/start` endpoint to accept new parameters
  - Update `/api/download/file/{task_id}` endpoint to return correct MIME type for MP3 files
- **Frontend:**
  - Add "Media Type" dropdown (Video/Audio)
  - Add "Audio Quality" dropdown (visible only when Audio is selected)
  - Hide "Resolution" dropdown when Audio is selected
  - Hide "Format" dropdown when Audio is selected (always MP3)
  - Update download button text to reflect media type being downloaded
  - Store video info in session state to persist across UI interactions
  - Ensure download button uses correct media_type from the actual download operation
- **Backend Addition:**
  - Fix filename generation for audio downloads to properly generate .mp3 extension after FFmpeg conversion

## Impact
- **Affected specs:** `video-download`
- **Affected code:**
  - `backend/main.py`: New parameters, audio download logic, FFmpeg post-processors
  - `frontend/app.py`: New dropdowns, conditional UI logic, dynamic button text, session state management
- **Dependencies:** No new Python packages (uses existing yt-dlp FFmpeg integration)
