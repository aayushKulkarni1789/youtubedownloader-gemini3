# Spec Delta: add-format-selector

## Modified Requirements

No modified requirements for video-download spec.

## Added Requirements

### ADDED Requirements

### Requirement: Resolution Selection
The system SHALL provide the ability to select the desired video resolution for downloads.

#### Scenario: User selects resolution
- **WHEN** the user accesses the YouTube Downloader
- **AND** the user selects "Video" as the media type
- **THEN** a Resolution selection dropdown is displayed
- **AND** the options are "Best", "1080p", "720p", "480p", "360p"
- **AND** "Best" is selected by default

### Requirement: Format Selection
The system SHALL provide the ability to select the desired output format for the downloaded video file.

#### Scenario: User selects video format
- **WHEN** the user accesses the YouTube Downloader
- **AND** the user selects "Video" as the media type
- **THEN** a Format selection dropdown is displayed
- **AND** the options are "mp4", "mkv", "webm"
- **AND** "mp4" is selected by default