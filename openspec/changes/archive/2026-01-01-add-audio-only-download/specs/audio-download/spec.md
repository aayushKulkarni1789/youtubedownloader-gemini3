# Audio Download Capability

This spec describes the audio download functionality of the YouTube downloader.

## ADDED Requirements

### Requirement: Audio Metadata
The system SHALL embed metadata in audio files from YouTube video information.

#### Scenario: Metadata is embedded in audio
- **GIVEN** the user downloads audio from a YouTube video
- **WHEN** the download and conversion is complete
- **THEN** the audio file contains metadata fields:
  - Title from video title
  - Artist from video uploader/channel
  - Album (YouTube video)
- **AND** the metadata is readable by audio players

### Requirement: Download File Retrieval
The system SHALL provide a way for users to retrieve the completed audio file.

#### Scenario: Save audio file after download
- **GIVEN** the audio download has completed successfully
- **WHEN** the user clicks the "Save Audio" button
- **THEN** the browser displays a save dialog
- **AND** the user can choose the location to save the file
- **AND** the file is saved with an .mp3 extension

### Requirement: MP3 Filename Generation
The system SHALL generate proper MP3 filenames for audio downloads after conversion.

#### Scenario: Audio file has correct MP3 filename
- **GIVEN** the user downloads audio from a YouTube video
- **WHEN** the download and MP3 conversion is complete
- **THEN** the file has a .mp3 extension
- **AND** the filename is based on the video title
- **AND** the filename is properly encoded for the filesystem