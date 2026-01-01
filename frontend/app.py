import streamlit as st
import requests
import time
import os

BACKEND_URL = "http://localhost:8000"

st.set_page_config(page_title="YouTube Downloader", page_icon="📹")

st.title("📹 YouTube Downloader")
st.write("Enter a YouTube URL below to download video or audio.")

# Initialize session state for video info persistence
if "video_info" not in st.session_state:
    st.session_state.video_info = None

video_url = st.text_input("YouTube URL", placeholder="https://www.youtube.com/watch?v=...")

if st.button("Get Video Info"):
    if not video_url:
        st.error("Please enter a valid URL.")
    else:
        try:
            response = requests.get(f"{BACKEND_URL}/api/info", params={"url": video_url})
            if response.status_code == 200:
                info = response.json()
                st.session_state.video_info = info  # Store in session state
            else:
                st.error(f"Failed to get video info: {response.text}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Display video info from session state if available
if st.session_state.video_info:
    info = st.session_state.video_info
    st.subheader("Video Information")
    st.image(info["thumbnail"], width=200)
    st.write(f"**Title:** {info['title']}")
    st.write(f"**Channel:** {info['uploader']}")
    st.write(f"**Views:** {info['views']}")
    st.write(f"**Duration:** {info['duration']} seconds")

    if st.button("Clear Info"):
        st.session_state.video_info = None

media_type = st.selectbox("Media Type", ["Video", "Audio"], index=0)

resolution = None
video_format = None
audio_quality = None

if media_type == "Video":
    resolution = st.selectbox("Resolution", ["Best", "1080p", "720p", "480p", "360p"], index=0)
    video_format = st.selectbox("Format", ["mp4", "mkv", "webm"], index=0)
else:
    audio_quality = st.selectbox(
        "Audio Quality", ["Best", "320kbps", "256kbps", "192kbps", "128kbps"], index=0
    )

if "task_id" not in st.session_state:
    st.session_state.task_id = None
if "download_file" not in st.session_state:
    st.session_state.download_file = None

if st.button(f"Download {media_type}"):
    if not video_url:
        st.error("Please enter a valid URL.")
    else:
        try:
            # Start download
            with st.spinner("Starting download..."):
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
                    st.session_state.download_file = None  # Reset previous download
                else:
                    st.error(f"Failed to start download: {response.text}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

if st.session_state.task_id:
    progress_bar = st.progress(0)
    status_text = st.empty()

    while True:
        try:
            response = requests.get(
                f"{BACKEND_URL}/api/download/progress/{st.session_state.task_id}"
            )
            if response.status_code == 200:
                data = response.json()
                status = data.get("status")
                progress = data.get("progress", 0.0)

                # Ensure progress is within bounds for st.progress
                display_progress = int(progress)
                if display_progress < 0:
                    display_progress = 0
                if display_progress > 100:
                    display_progress = 100

                progress_bar.progress(display_progress)
                status_text.text(f"Status: {status} ({progress}%)")

                if status == "completed":
                    st.success("Download completed!")
                    # Fetch file
                    with st.spinner("Retrieving file..."):
                        file_response = requests.get(
                            f"{BACKEND_URL}/api/download/file/{st.session_state.task_id}"
                        )
                        if file_response.status_code == 200:
                            # Get filename
                            content_disposition = file_response.headers.get("content-disposition")
                            filename = "video.mp4"
                            if content_disposition:
                                try:
                                    filename = content_disposition.split("filename=")[1].strip('"')
                                except:
                                    pass

                            st.session_state.download_file = {
                                "data": file_response.content,
                                "filename": filename,
                                "mime": file_response.headers.get("content-type", "video/mp4"),
                                "media_type": media_type,  # Store the media type used for this download
                            }
                            st.session_state.task_id = None  # Clear task
                            st.rerun()
                    break
                elif status == "error":
                    st.error(f"Download failed: {data.get('error')}")
                    st.session_state.task_id = None
                    break

                time.sleep(1)
            else:
                st.error("Failed to get progress.")
                break
        except Exception as e:
            st.error(f"Error polling progress: {e}")
            break

if st.session_state.download_file:
    st.success("File processed successfully! Click below to save.")
    st.download_button(
        label=f"💾 Save {st.session_state.download_file['media_type'].capitalize()}",
        data=st.session_state.download_file["data"],
        file_name=st.session_state.download_file["filename"],
        mime=st.session_state.download_file["mime"],
    )

st.markdown("---")
st.caption("Powered by FastAPI and Streamlit")
