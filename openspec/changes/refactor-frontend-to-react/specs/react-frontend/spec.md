## ADDED Requirements

### Requirement: React Frontend Architecture
The frontend SHALL be implemented as a React single-page application using Vite, TypeScript, and modern tooling.

#### Scenario: Project initialization
- **WHEN** the project is set up
- **THEN** the frontend uses React 18+ with TypeScript
- **AND** Vite is used as the build tool
- **AND** the project supports hot module replacement during development

#### Scenario: API communication
- **WHEN** the frontend communicates with the backend
- **THEN** requests are made to the FastAPI backend via `/api/*` endpoints
- **AND** TypeScript interfaces ensure type-safe API responses
- **AND** a Vite proxy forwards requests to `http://localhost:8000` during development

### Requirement: Component-Based UI Structure
The frontend SHALL use a modular component architecture for maintainability.

#### Scenario: Component organization
- **WHEN** the UI is rendered
- **THEN** distinct components handle: URL input, video preview, download configuration, progress display, and save action
- **AND** each component manages its own presentation logic
- **AND** shared state is managed via a central store

### Requirement: State Management
The frontend SHALL use Zustand for global application state.

#### Scenario: State persistence across components
- **WHEN** video info is fetched or download is started
- **THEN** the state is stored in Zustand
- **AND** all components can access the current video info, task ID, and download status
- **AND** state updates trigger re-renders only in affected components

### Requirement: Progress Polling with TanStack Query
The frontend SHALL use TanStack Query for efficient progress polling.

#### Scenario: Polling during download
- **WHEN** a download is in progress
- **THEN** the frontend polls `/api/download/progress/{task_id}` every second
- **AND** polling automatically stops when status is "completed" or "error"
- **AND** the UI remains responsive during polling

### Requirement: Tailwind CSS Styling
The frontend SHALL use Tailwind CSS for styling with a custom dark theme.

#### Scenario: Visual consistency with original design
- **WHEN** the UI is displayed
- **THEN** the dark background (#0F0F0F) and red accent (#FF0000) colors are applied
- **AND** Oswald font is used for headings
- **AND** Lato font is used for body text
- **AND** buttons have gradient backgrounds with hover effects
