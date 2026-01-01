# Video Download Capability

This spec describes the video download functionality of the YouTube downloader.

## ADDED Requirements

### Requirement: URL Input
The system SHALL allow users to input a YouTube video URL.

#### Scenario: User enters video URL
- **GIVEN** the user is on the download page
- **WHEN** the user enters a valid YouTube URL in the input field
- **THEN** the URL is validated
- **AND** the user can proceed to download

### Requirement: Video Metadata Display
The system SHALL display metadata about the video before download.

#### Scenario: Video information is retrieved
- **GIVEN** the user has entered a valid YouTube URL
- **WHEN** the user clicks "Get Video Info"
- **THEN** the system fetches video metadata
- **AND** displays thumbnail, title, channel, views, and duration