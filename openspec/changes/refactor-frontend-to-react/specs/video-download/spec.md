## MODIFIED Requirements

### Requirement: Media Type Selection
The system SHALL allow users to choose between video and audio download modes.

#### Scenario: Select video download mode
- **WHEN** the user selects "Video" from the media type dropdown
- **THEN** the resolution dropdown is visible
- **AND** the format dropdown is visible
- **AND** the audio quality dropdown is hidden (not applicable for video)

#### Scenario: UI implementation
- **WHEN** media type selection is rendered
- **THEN** a React select component provides the options
- **AND** selection updates the Zustand store
- **AND** dependent dropdowns conditionally render based on selection

### Requirement: Real-time Download Progress
The system SHALL provide real-time progress updates during video downloads.

#### Scenario: Display video download progress
- **WHEN** a video download is in progress
- **THEN** a progress bar displays the download progress
- **AND** the percentage completed is shown
- **AND** status text indicates the current state (downloading, processing, completed)

#### Scenario: React implementation
- **WHEN** download progress is displayed
- **THEN** TanStack Query polls the progress endpoint
- **AND** the progress bar component receives updates via query state
- **AND** polling stops automatically when download completes or errors

### Requirement: Download Button Behavior
The system SHALL provide a save button after video download completion.

#### Scenario: Save downloaded video
- **WHEN** a video download is completed
- **THEN** a "Save Video" button is displayed
- **AND** when clicked, it triggers the browser's save dialog
- **AND** the user can choose the save location

#### Scenario: React file download implementation
- **WHEN** the save button is clicked
- **THEN** the file is fetched as a blob
- **AND** the filename is extracted from the Content-Disposition header
- **AND** a temporary object URL triggers the download
- **AND** the object URL is revoked after download
