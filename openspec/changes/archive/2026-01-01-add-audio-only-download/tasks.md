## 1. Backend Implementation
- [x] 1.1 Add AUDIO_QUALITY_MAP constant in backend/main.py
- [x] 1.2 Update run_download() function to accept media_type and audio_quality parameters
- [x] 1.3 Implement audio-only download path with FFmpeg post-processor for MP3 conversion
- [x] 1.4 Add FFmpeg metadata post-processor for embedding title and artist
- [x] 1.5 Update /api/download/start endpoint to accept media_type and audio_quality parameters
- [x] 1.6 Update /api/download/file/{task_id} endpoint to return audio/mpeg for MP3 files

## 2. Frontend Implementation
- [x] 2.1 Add media_type selectbox (Video/Audio) before resolution selector
- [x] 2.2 Add audio_quality selectbox (Best/320kbps/256kbps/192kbps/128kbps) with conditional display
- [x] 2.3 Implement conditional UI to hide resolution dropdown when Audio selected
- [x] 2.4 Implement conditional UI to hide format dropdown when Audio selected
- [x] 2.5 Update "Download Video" button text to be dynamic (Download Video/Download Audio)
- [x] 2.6 Update API call to include media_type and audio_quality parameters
- [x] 2.7 Update download button label to match media type
- [x] 2.8 Add session state for video info persistence
- [x] 2.9 Update video info display to use session state
- [x] 2.10 Add "Clear Info" button
- [x] 2.11 Store media_type in download_file session state
- [x] 2.12 Update download button to use stored media_type
- [x] 2.13 Backend: Fix filename generation for audio downloads (MP3 conversion)

## 3. Testing Setup
- [x] 3.1 Create test_videos.txt with sample YouTube links for testing
- [x] 3.2 Test audio downloads with all quality settings (Best, 320kbps, 256kbps, 192kbps, 128kbps)
- [x] 3.3 Verify metadata is embedded in downloaded MP3 files
- [x] 3.4 Test video downloads still work correctly with all resolutions and formats
- [x] 3.5 Verify UI properly shows/hides controls when switching between Audio and Video modes
