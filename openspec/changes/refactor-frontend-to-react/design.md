## Context
The current frontend uses Streamlit, a Python framework for data apps. While easy to prototype, Streamlit has limitations:
- Page reruns on every interaction (not true SPA behavior)
- Limited control over styling and animations
- Polling requires while-loops that block the main thread
- No separation of concerns (UI logic mixed with state)

Migrating to React provides a modern SPA experience with better UX, maintainability, and performance.

## Goals / Non-Goals

### Goals
- Replicate all existing functionality in React
- Maintain the same visual design (dark theme, red accents, Oswald/Lato fonts)
- Improve user experience with smoother interactions
- Type-safe API integration with TypeScript
- Efficient progress polling without blocking UI
- Clean separation of components and state

### Non-Goals
- Changing the backend API (FastAPI stays unchanged)
- Adding new features (this is a pure refactor)
- Mobile-first responsive design (keep desktop-focused like current)
- Server-side rendering (client-side SPA is sufficient)

## Decisions

### 1. Build Tool: Vite + TypeScript
**Decision**: Use Vite with React + TypeScript template
**Rationale**: 
- Vite is the modern standard (CRA is deprecated)
- TypeScript ensures type safety for API responses
- Fast HMR for development

### 2. State Management: Zustand
**Decision**: Use Zustand for global state
**Rationale**:
- Simpler than Redux for this scale
- Works well outside React tree
- Minimal boilerplate
- State needed: `videoInfo`, `taskId`, `downloadFile`

### 3. Data Fetching: TanStack Query v5
**Decision**: Use TanStack Query for API calls and polling
**Rationale**:
- Built-in polling with `refetchInterval`
- Automatic retry and error handling
- Query caching
- Clean separation from UI components

### 4. Styling: Tailwind CSS
**Decision**: Use Tailwind CSS for styling
**Rationale**:
- Utility-first approach matches the custom CSS patterns in current app
- Easy to replicate the dark theme
- No CSS-in-JS runtime overhead
- Custom theme extension for brand colors

### 5. Component Architecture
```
frontend-react/
├── src/
│   ├── components/
│   │   ├── Header.tsx           # Hero title section
│   │   ├── UrlInput.tsx         # URL input + Fetch button
│   │   ├── VideoPreview.tsx     # Thumbnail, title, stats
│   │   ├── DownloadConfig.tsx   # Media type, resolution, format selectors
│   │   ├── DownloadProgress.tsx # Progress bar during download
│   │   └── SaveButton.tsx       # Final save file button
│   ├── hooks/
│   │   ├── useVideoInfo.ts      # Fetch video metadata
│   │   ├── useDownload.ts       # Start download mutation
│   │   └── useProgress.ts       # Poll progress with auto-stop
│   ├── store/
│   │   └── downloadStore.ts     # Zustand store
│   ├── api/
│   │   └── client.ts            # API client with types
│   ├── types/
│   │   └── api.ts               # TypeScript interfaces
│   ├── App.tsx                  # Main app component
│   ├── main.tsx                 # Entry point
│   └── index.css                # Tailwind imports + custom fonts
├── index.html
├── vite.config.ts               # Vite config with proxy
├── tailwind.config.js           # Custom theme
├── tsconfig.json
└── package.json
```

### 6. API Proxy Configuration
**Decision**: Use Vite's dev server proxy
**Rationale**:
- Avoids CORS issues during development
- `/api/*` proxied to `http://localhost:8000`
- Production can use nginx reverse proxy

## Risks / Trade-offs

| Risk | Mitigation |
|------|------------|
| Learning curve for maintainers unfamiliar with React | Comprehensive code comments, simple architecture |
| More complex build process | Automated via `start.sh`, production builds are static files |
| Larger initial bundle size | Vite's tree-shaking keeps it minimal |
| Loss of Streamlit's quick prototyping | Justified by improved UX and maintainability |

## Migration Plan

1. Create `frontend-react/` alongside existing `frontend/`
2. Implement all components and test against running backend
3. Update `start.sh` to support both modes (flag or env var)
4. Remove `frontend/app.py` and Streamlit dependency
5. Update documentation

## Open Questions
- Should we keep Streamlit as a fallback? (Recommendation: No, clean break)
- Port for React dev server? (Recommendation: 5173, proxy API to 8000)
