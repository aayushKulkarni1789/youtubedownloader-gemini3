# Project Context

## Purpose
A modern, fast, and easy-to-use YouTube video downloader web application. It provides a simple interface for users to input a YouTube URL and download the video directly to their device, utilizing `yt-dlp` for efficient processing.

## Tech Stack
- **Language:** Python 3.12+, TypeScript
- **Frontend:** React 19, Vite, TailwindCSS, TanStack Query, Zustand
- **Backend:** FastAPI, Uvicorn
- **Core Library:** yt-dlp
- **Package Manager:** uv (Python), npm (Node.js)

## Project Conventions

### Code Style
- Follow standard Python conventions (PEP 8).
- Use type hints for function arguments and return values, especially in FastAPI endpoints.
- Use `uv` for managing Python dependencies and virtual environments.
- Use TypeScript with strict mode for frontend code.
- Use TailwindCSS for styling (no inline styles).

### Architecture Patterns
- **Frontend-Backend Separation:** React app (`frontend-react/`) communicates with the FastAPI backend (`backend/main.py`) via HTTP requests through Vite proxy.
- **Asynchronous Processing:** The backend handles video downloads asynchronously and uses background tasks for cleaning up temporary files.
- **Temporary Storage:** Downloaded files are temporarily stored in a `downloads/` directory before being served to the user.
- **State Management:** Zustand for global client state, TanStack Query for server state and caching.

### Testing Strategy
- Use `pytest` for backend unit and integration tests.
- Verify backend endpoints (`/health`, `/api/info`, `/api/download/*`) and frontend interaction.

### Git Workflow
- Standard feature branch workflow.
- Commit messages should be clear and descriptive.

## Domain Context
- The application acts as a wrapper around `yt-dlp`, exposing its functionality through a web interface.
- Understanding of `yt-dlp` options and configurations is crucial for extending download capabilities.

## Important Constraints
- **Legal:** This tool is for educational purposes only. Users must respect YouTube's Terms of Service and copyright laws.
- **Performance:** Video processing can be resource-intensive; large files may take time to download and process.
- **Storage:** The `downloads/` directory is temporary; mechanisms are in place to clean up files after serving.

## External Dependencies
- **YouTube:** The primary source of content. Changes to YouTube's algorithms or API may affect `yt-dlp` functionality.
