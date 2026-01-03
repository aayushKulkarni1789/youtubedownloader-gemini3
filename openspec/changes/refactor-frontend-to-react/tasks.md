## 1. Project Setup
- [x] 1.1 Initialize React + TypeScript project with Vite in `frontend-react/`
- [x] 1.2 Install dependencies: tailwindcss, @tanstack/react-query, zustand
- [x] 1.3 Configure Tailwind with custom theme (colors, fonts)
- [x] 1.4 Configure Vite proxy for `/api` to `http://localhost:8000`
- [x] 1.5 Add Google Fonts (Oswald, Lato) to index.html

## 2. Core Infrastructure
- [x] 2.1 Create TypeScript types for API responses (`types/api.ts`)
- [x] 2.2 Create API client with fetch wrapper (`api/client.ts`)
- [x] 2.3 Create Zustand store for download state (`store/downloadStore.ts`)
- [x] 2.4 Set up TanStack Query provider in App.tsx

## 3. Components Implementation
- [x] 3.1 Create Header component with hero title styling
- [x] 3.2 Create UrlInput component with fetch button
- [x] 3.3 Create VideoPreview component (thumbnail, title, stats)
- [x] 3.4 Create DownloadConfig component (media type, resolution, format, quality selectors)
- [x] 3.5 Create DownloadProgress component with progress bar
- [x] 3.6 Create SaveButton component for file download

## 4. Hooks Implementation
- [x] 4.1 Create useVideoInfo hook (TanStack Query mutation)
- [x] 4.2 Create useDownload hook (start download mutation)
- [x] 4.3 Create useProgress hook (polling with auto-stop on completion/error)

## 5. App Integration
- [x] 5.1 Wire up all components in App.tsx
- [x] 5.2 Implement conditional rendering based on state
- [x] 5.3 Add file download handling (blob + object URL)
- [x] 5.4 Add error handling and loading states

## 6. Styling & Polish
- [x] 6.1 Apply dark theme with gradient backgrounds
- [x] 6.2 Style buttons with red gradient and hover effects
- [x] 6.3 Style progress bar with animated stripes
- [x] 6.4 Add balloons/confetti effect on download complete (optional)
- [x] 6.5 Hide scrollbars and add smooth transitions

## 7. Build & Deployment
- [x] 7.1 Update `start.sh` to run React dev server
- [x] 7.2 Configure production build output
- [x] 7.3 Update `requirements.txt` (remove streamlit)
- [x] 7.4 Update `openspec/project.md` with new tech stack
- [x] 7.5 Update `README.md` with new setup instructions

## 8. Testing & Validation
- [x] 8.1 Test video info fetching
- [x] 8.2 Test video download with all resolution/format combinations
- [x] 8.3 Test audio download with all quality options
- [x] 8.4 Test progress polling and auto-stop
- [x] 8.5 Test file save functionality
- [x] 8.6 Test error handling (invalid URL, network errors)

## 9. Cleanup
- [x] 9.1 Remove `frontend/app.py`
- [x] 9.2 Remove `frontend/` directory
- [ ] 9.3 Rename `frontend-react/` to `frontend/` (optional, or keep separate)
