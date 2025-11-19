# 📹 YouTube Video Downloader

> [!NOTE]
> This project was completely made by Opencode and Gemini 3 Pro. From installing the required packages, to writing the code, to literally making and pushing this code to a public repo (I did not even give it my github username), all the things were handled by the agent. This model is insane. The only human made part in this entire project is this note that you are reading at the moment.

A modern, fast, and easy-to-use YouTube video downloader web application built with **FastAPI** and **Streamlit**.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.22%2B-red)

## 🌟 Features

- **Simple Interface:** Clean and intuitive UI powered by Streamlit.
- **Fast Downloads:** Efficient video processing using `yt-dlp`.
- **Direct Download:** Download videos directly to your device.
- **Background Processing:** Backend handles downloads asynchronously.

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed:
- **Python 3.8+**
- **[uv](https://github.com/astral-sh/uv):** An extremely fast Python package installer and resolver.

### Installation & Usage

1.  **Clone the repository** (if applicable) or download the source code.

2.  **Run the startup script**:
    The included script creates a virtual environment, installs dependencies using `uv`, and starts the services.

    ```bash
    ./start.sh
    ```

3.  **Access the application**:
    -   **Frontend (UI):** [http://localhost:8501](http://localhost:8501)
    -   **Backend (API Docs):** [http://localhost:8000/docs](http://localhost:8000/docs)

## 🏗️ Project Structure

```text
youtubedownloader/
├── backend/
│   └── main.py          # FastAPI application & logic
├── frontend/
│   └── app.py           # Streamlit user interface
├── downloads/           # Temporary storage for downloaded videos
├── requirements.txt     # Python dependencies
├── start.sh             # Startup script
└── README.md            # Project documentation
```

## 🛠️ Technologies

-   **[FastAPI](https://fastapi.tiangolo.com/):** High-performance web framework for building APIs.
-   **[Streamlit](https://streamlit.io/):**  Turns data scripts into shareable web apps in minutes.
-   **[yt-dlp](https://github.com/yt-dlp/yt-dlp):**  A command-line program to download videos from YouTube.

---

_Note: This tool is for educational purposes only. Please respect YouTube's Terms of Service and copyright laws._
