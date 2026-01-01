# Specs Tree

This document shows the hierarchical structure of all specifications across completed changes.

## Overview

- **add-format-selector**: Format selection for video/audio downloads
- **add-progress-bar**: Real-time download progress tracking
- **add-video-statistics**: Video/metadata fetching and display
- **add-audio-only-download**: Audio-only downloads with quality selection

## Specification Structure

### video-download Spec
`openspec/specs/video-download/spec.md`

#### Requirements
- Resolution Selection
  - Select Best resolution
  - Select 1080p resolution
  - Select 720p resolution
  - Select 480p resolution
  - Select 360p resolution
- Format Selection
  - Select MP4 format
  - Select MKV format
  - Select WebM format
- Real-time Download Progress
  - Display video download progress
  - Display download percentage
  - Display download status
  - Handle download errors
- Video Metadata Display
  - Fetch video metadata
  - Display video title
  - Display video channel/uploader
  - Display video view count
  - Display video duration
  - Display video thumbnail
- Video Info Persistence
  - Video info persists across dropdown changes
  - Clear video info
- Download Button Behavior
  - Save downloaded video
  - Show correct media type in button label
  - Proper filename for video files

### audio-download Spec
`openspec/specs/audio-download/spec.md`

#### Requirements
- Media Type Selection
  - Select audio download mode
  - Hide resolution/format when audio selected
- Audio Quality Selection
  - Select Best quality
  - Select 320kbps quality
  - Select 256kbps quality
  - Select 192kbps quality
  - Select 128kbps quality
- Audio Post-Processing
  - Convert audio to MP3
  - Apply quality/bitrate settings
  - Embed metadata (title, artist, uploader, album)
- Real-time Download Progress
  - Display audio download progress
  - Display download percentage
  - Display download status
- Download Button Behavior
  - Save downloaded audio
  - Show correct media type in button label
  - Proper MP3 filename after conversion
- Metadata Display
  - Display audio metadata

## Changes and Their Spec Contributions

### 1. add-format-selector (Archived: 2025-11-19)
**Specs Modified:**
- `video-download`: Added Resolution Selection, Format Selection requirements
- `audio-download`: Added Media Type Selection (audio mode)

### 2. add-progress-bar (In Progress)
**Specs Modified:**
- `video-download`: Added Real-time Download Progress requirements
- `audio-download`: Added Real-time Download Progress requirements

### 3. add-video-statistics (In Progress)
**Specs Modified:**
- `video-download`: Added Video Metadata Display requirements
- `audio-download`: Added Metadata Display requirements

### 4. add-audio-only-download (In Progress)
**Specs Modified:**
- `video-download`: Added Video Info Persistence, Download Button Behavior (video-specific)
- `audio-download`: Added Media Type Selection, Audio Quality Selection, Audio Post-Processing, Download Button Behavior (audio-specific)

## Spec Relationships

- **video-download spec**: Defines all requirements specific to video download functionality
- **audio-download spec**: Defines all requirements specific to audio download functionality
- **Shared requirements**: Some requirements (like progress tracking, metadata display) apply to both video and audio downloads