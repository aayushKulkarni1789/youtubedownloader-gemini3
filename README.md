# YouTube Video Downloader

> [!NOTE]
> This project was completely made by Opencode and Gemini 3 Pro. From installing the required packages, to writing the code, to literally making and pushing this code to a public repo (I did not even give it my github username), all the things were handled by the agent. This model is insane. The only human made part in this entire project is this note that you are reading at the moment.

A modern, fast, and easy-to-use YouTube video downloader web application built with **FastAPI** and **React**.

![Python](https://img.shields.io/badge/Python-3.12%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-green)
![React](https://img.shields.io/badge/React-19-blue)
![TypeScript](https://img.shields.io/badge/TypeScript-5.6-blue)

## Features

- **Modern UI:** Clean and responsive interface built with React and TailwindCSS
- **Video & Audio Downloads:** Choose between video (mp4, mkv, webm) or audio-only (mp3)
- **Quality Selection:** Select resolution (1080p, 720p, 480p, 360p) or audio bitrate
- **Real-time Progress:** Live download progress with percentage and status
- **Fast Downloads:** Efficient video processing using `yt-dlp`

## Getting Started

### Prerequisites

Ensure you have the following installed:
- **Python 3.12+**
- **Node.js 18+**
- **[uv](https://github.com/astral-sh/uv):** An extremely fast Python package installer and resolver.

### Installation & Usage

1.  **Clone the repository** (if applicable) or download the source code.

2.  **Run the startup script**:
    The included script creates a virtual environment, installs dependencies, and starts both services.

    ```bash
    ./start.sh
    ```

3.  **Access the application**:
    -   **Frontend (UI):** [http://localhost:5173](http://localhost:5173)
    -   **Backend (API Docs):** [http://localhost:8000/docs](http://localhost:8000/docs)

## Project Structure

```text
youtubedownloader/
├── backend/
│   ├── main.py           # FastAPI application & logic
│   └── tests/            # Backend tests
├── frontend-react/
│   ├── src/
│   │   ├── api/          # API client
│   │   ├── components/   # React components
│   │   ├── hooks/        # Custom React hooks
│   │   ├── providers/    # Context providers
│   │   ├── store/        # Zustand state management
│   │   └── types/        # TypeScript types
│   └── package.json      # Node.js dependencies
├── downloads/            # Temporary storage for downloaded videos
├── requirements.txt      # Python dependencies
├── start.sh              # Startup script
└── README.md             # Project documentation
```

## Technologies

-   **[FastAPI](https://fastapi.tiangolo.com/):** High-performance web framework for building APIs.
-   **[React](https://react.dev/):** Modern UI library for building user interfaces.
-   **[Vite](https://vitejs.dev/):** Next generation frontend tooling.
-   **[TailwindCSS](https://tailwindcss.com/):** Utility-first CSS framework.
-   **[TanStack Query](https://tanstack.com/query):** Powerful data fetching and caching.
-   **[Zustand](https://zustand-demo.pmnd.rs/):** Lightweight state management.
-   **[yt-dlp](https://github.com/yt-dlp/yt-dlp):** A command-line program to download videos from YouTube.

---

_Note: This tool is for educational purposes only. Please respect YouTube's Terms of Service and copyright laws._
