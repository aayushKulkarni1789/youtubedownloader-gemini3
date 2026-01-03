# Change: Refactor Frontend from Streamlit to React

## Why
The current Streamlit frontend, while functional, has limitations for building a modern, responsive UI with rich user interactions. React provides better control over component lifecycle, state management, and enables a more polished user experience with modern tooling (Vite, TypeScript, TanStack Query).

## What Changes
- **BREAKING**: Replace Streamlit frontend (`frontend/app.py`) with a React + TypeScript application
- New React frontend in `frontend-react/` directory using Vite
- Tailwind CSS for styling (replicating the current dark theme with red accents)
- TanStack Query for efficient API polling during downloads
- Zustand for lightweight state management
- Component-based architecture with type-safe API integration
- Backend (FastAPI) remains unchanged - no API modifications required
- Update `start.sh` to serve React app in development mode

## Impact
- Affected specs: `video-download`, `audio-download` (UI requirements remain same, implementation changes)
- Affected code:
  - Remove: `frontend/app.py`
  - Add: `frontend-react/` (new React application)
  - Modify: `start.sh` (updated startup script)
  - Modify: `openspec/project.md` (update tech stack)
  - Modify: `requirements.txt` (remove streamlit)
