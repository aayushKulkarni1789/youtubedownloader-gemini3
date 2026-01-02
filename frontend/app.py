import streamlit as st
import requests
import time
import os

BACKEND_URL = "http://localhost:8000"

st.set_page_config(page_title="YouTube Downloader", page_icon="📹", layout="centered")

st.markdown(
    """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;700&family=Lato:wght@300;400;700&display=swap');

    /* --- ROOT VARIABLES --- */
    :root {
        --primary-color: #FF0000;
        --primary-dark: #CC0000;
        --bg-color: #0F0F0F;
        --card-bg: #1E1E1E;
        --text-color: #FFFFFF;
        --text-secondary: #AAAAAA;
        --border-radius: 12px;
    }

    /* --- GENERAL SETTINGS --- */
    .stApp {
        background-color: var(--bg-color);
        background-image: 
            radial-gradient(ellipse at 20% 80%, rgba(255, 0, 0, 0.08) 0%, transparent 50%),
            radial-gradient(ellipse at 80% 20%, rgba(100, 0, 150, 0.06) 0%, transparent 50%),
            radial-gradient(ellipse at center, transparent 0%, #0F0F0F 70%);
        font-family: 'Lato', sans-serif;
        color: var(--text-color);
    }
    
    h1, h2, h3 {
        font-family: 'Oswald', sans-serif;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    h1 {
        font-size: 3rem;
        font-weight: 700;
        background: -webkit-linear-gradient(45deg, #FF0000, #FFFFFF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }

    .stMarkdown p {
        color: var(--text-secondary);
        font-size: 1.1rem;
    }

    /* --- HIDE DEFAULT STREAMLIT UI --- */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* --- INPUT FIELDS --- */
    .stTextInput > div > div > input {
        background-color: var(--card-bg);
        color: var(--text-color);
        border: 1px solid #333;
        border-radius: var(--border-radius);
        padding: 12px 15px;
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: var(--primary-color);
        box-shadow: 0 0 10px rgba(255, 0, 0, 0.2);
    }

    /* --- BUTTONS --- */
    .stButton > button {
        background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-dark) 100%);
        color: white;
        border: none;
        border-radius: var(--border-radius);
        padding: 0.6rem 1.5rem;
        font-weight: 700;
        font-family: 'Oswald', sans-serif;
        letter-spacing: 1px;
        text-transform: uppercase;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255, 0, 0, 0.3);
        width: 100%;
    }

    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(255, 0, 0, 0.5);
        color: white;
    }

    .stButton > button:active {
        transform: translateY(-1px);
    }

    /* --- SELECT BOXES --- */
    .stSelectbox label {
        color: var(--text-secondary) !important;
        font-family: 'Oswald', sans-serif;
        text-transform: uppercase;
        font-size: 0.8rem;
    }
    
    .stSelectbox > div > div {
        background-color: var(--card-bg);
        color: var(--text-color);
        border: 1px solid #333;
        border-radius: var(--border-radius);
    }

    /* --- ALERTS & MESSAGES --- */
    .stAlert {
        background-color: var(--card-bg);
        border: 1px solid #333;
        border-radius: var(--border-radius);
        color: var(--text-color);
    }

    /* --- PROGRESS BAR --- */
    .stProgress > div > div > div > div {
        background-color: var(--primary-color);
        background-image: linear-gradient(45deg, rgba(255,255,255,.15) 25%, transparent 25%, transparent 50%, rgba(255,255,255,.15) 50%, rgba(255,255,255,.15) 75%, transparent 75%, transparent);
        background-size: 1rem 1rem;
    }

    /* --- UTILITY CLASSES --- */
    .video-title {
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
        color: #fff;
    }
    
    .video-stats {
        font-size: 0.9rem;
        color: #888;
        display: flex;
        gap: 15px;
        margin-bottom: 1rem;
    }

    .stat-item {
        background: #252525;
        padding: 4px 8px;
        border-radius: 4px;
    }

    .hero-container {
        text-align: center;
        padding: 40px 0;
    }

    /* Fix button alignment with input */
    [data-testid="stHorizontalBlock"] {
        align-items: flex-end;
    }

    /* Ensure button matches input height */
    .stTextInput > div > div > input {
        height: 42px;
    }

    .stButton > button {
        height: 42px;
        margin-bottom: 0;
    }
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="hero-container"><h1>YOUTUBE DOWNLOADER</h1><p>Premium Video & Audio Extraction Tool</p></div>',
    unsafe_allow_html=True,
)

if "video_info" not in st.session_state:
    st.session_state.video_info = None

if "task_id" not in st.session_state:
    st.session_state.task_id = None
if "download_file" not in st.session_state:
    st.session_state.download_file = None

col1, col2 = st.columns([4, 1])
with col1:
    video_url = st.text_input(
        "YouTube URL", placeholder="Paste YouTube link here...", label_visibility="collapsed"
    )
with col2:
    st.markdown("<div style='margin-top: 0px;'></div>", unsafe_allow_html=True)
    if st.button("FETCH INFO"):
        if not video_url:
            st.error("Please enter a URL first.")
        else:
            try:
                with st.spinner("Fetching video details..."):
                    response = requests.get(f"{BACKEND_URL}/api/info", params={"url": video_url})
                    if response.status_code == 200:
                        info = response.json()
                        st.session_state.video_info = info
                        st.session_state.task_id = None
                        st.session_state.download_file = None
                    else:
                        st.error(f"Error: {response.text}")
            except Exception as e:
                st.error(f"Connection error: {e}")

if st.session_state.video_info:
    info = st.session_state.video_info

    st.markdown("---")

    vid_col1, vid_col2 = st.columns([1, 2])

    with vid_col1:
        st.image(info["thumbnail"], use_container_width=True)

    with vid_col2:
        st.markdown(f'<div class="video-title">{info["title"]}</div>', unsafe_allow_html=True)
        st.markdown(
            f"""
        <div class="video-stats">
            <span class="stat-item">👤 {info["uploader"]}</span>
            <span class="stat-item">👁️ {info["views"]:,} views</span>
            <span class="stat-item">⏱️ {info["duration"]}s</span>
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown("### ⚙️ CONFIGURATION", unsafe_allow_html=True)

        opt_col1, opt_col2, opt_col3 = st.columns(3)

        with opt_col1:
            media_type = st.selectbox("Type", ["Video", "Audio"], index=0)

        resolution = None
        video_format = None
        audio_quality = None

        if media_type == "Video":
            with opt_col2:
                resolution = st.selectbox(
                    "Quality", ["Best", "1080p", "720p", "480p", "360p"], index=0
                )
            with opt_col3:
                video_format = st.selectbox("Format", ["mp4", "mkv", "webm"], index=0)
        else:
            with opt_col2:
                audio_quality = st.selectbox(
                    "Bitrate", ["Best", "320kbps", "256kbps", "192kbps", "128kbps"], index=0
                )

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button(f"DOWNLOAD {media_type.upper()} NOW", use_container_width=True):
        if not video_url:
            st.error("Session expired, please re-enter URL.")
        else:
            try:
                with st.spinner("Initializing download sequence..."):
                    response = requests.post(
                        f"{BACKEND_URL}/api/download/start",
                        params={
                            "url": video_url,
                            "media_type": media_type.lower(),
                            "audio_quality": audio_quality,
                            "resolution": resolution,
                            "video_format": video_format,
                        },
                    )
                    if response.status_code == 200:
                        task_id = response.json()["task_id"]
                        st.session_state.task_id = task_id
                        st.session_state.download_file = None
                    else:
                        st.error(f"Failed to start: {response.text}")
            except Exception as e:
                st.error(f"Error: {e}")

if st.session_state.task_id:
    st.markdown("### 🚀 PROCESSING", unsafe_allow_html=True)
    progress_bar = st.progress(0)
    status_text = st.empty()

    result_container = st.container()

    while True:
        try:
            response = requests.get(
                f"{BACKEND_URL}/api/download/progress/{st.session_state.task_id}"
            )
            if response.status_code == 200:
                data = response.json()
                status = data.get("status")
                progress = data.get("progress", 0.0)

                display_progress = int(progress)
                display_progress = max(0, min(display_progress, 100))

                progress_bar.progress(display_progress)
                status_text.markdown(f"`Status: {status} ... {display_progress}%`")

                if status == "completed":
                    status_text.success("Processing Complete!")

                    with st.spinner("Finalizing file..."):
                        file_response = requests.get(
                            f"{BACKEND_URL}/api/download/file/{st.session_state.task_id}"
                        )
                        if file_response.status_code == 200:
                            content_disposition = file_response.headers.get("content-disposition")
                            filename = "downloaded_file"
                            if content_disposition:
                                try:
                                    filename = content_disposition.split("filename=")[1].strip('"')
                                except:
                                    pass

                            st.session_state.download_file = {
                                "data": file_response.content,
                                "filename": filename,
                                "mime": file_response.headers.get("content-type", "video/mp4"),
                                "media_type": "video"
                                if filename.endswith((".mp4", ".mkv", ".webm"))
                                else "audio",
                            }
                            st.session_state.task_id = None
                            st.rerun()
                    break
                elif status == "error":
                    st.error(f"Download failed: {data.get('error')}")
                    st.session_state.task_id = None
                    break

                time.sleep(1)
            else:
                st.error("Lost connection to progress tracker.")
                break
        except Exception as e:
            st.error(f"Polling error: {e}")
            break

if st.session_state.download_file:
    st.markdown("---")
    st.balloons()
    st.success("Your file is ready!")

    col_d1, col_d2, col_d3 = st.columns([1, 2, 1])
    with col_d2:
        st.download_button(
            label=f"💾 SAVE FILE ({st.session_state.download_file['filename']})",
            data=st.session_state.download_file["data"],
            file_name=st.session_state.download_file["filename"],
            mime=st.session_state.download_file["mime"],
            use_container_width=True,
        )

    if st.button("Download Another Video"):
        st.session_state.download_file = None
        st.session_state.video_info = None
        st.rerun()

st.markdown(
    """
<div class="footer" style="margin-top: 50px; text-align: center; color: #555;">
    <p>Powered by OpenCode | Gemini 3 Pro</p>
</div>
""",
    unsafe_allow_html=True,
)
