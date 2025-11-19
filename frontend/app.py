import streamlit as st
import requests
import os

BACKEND_URL = "http://localhost:8000"

st.set_page_config(page_title="YouTube Downloader", page_icon="📹")

st.title("📹 YouTube Video Downloader")
st.write("Enter a YouTube URL below to download the video.")

video_url = st.text_input("YouTube URL", placeholder="https://www.youtube.com/watch?v=...")

if st.button("Download Video"):
    if not video_url:
        st.error("Please enter a valid URL.")
    else:
        with st.spinner("Downloading... This might take a moment depending on the video length."):
            try:
                # Send request to backend
                response = requests.post(
                    f"{BACKEND_URL}/download", params={"url": video_url}, stream=True
                )

                if response.status_code == 200:
                    # Get filename from headers or default
                    content_disposition = response.headers.get("content-disposition")
                    filename = "video.mp4"
                    if content_disposition:
                        try:
                            filename = content_disposition.split("filename=")[1].strip('"')
                        except:
                            pass

                    st.success("Video processed successfully! Click below to save.")
                    st.download_button(
                        label="💾 Save Video",
                        data=response.content,
                        file_name=filename,
                        mime="video/mp4",
                    )
                else:
                    st.error(f"Error: {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {e}")

st.markdown("---")
st.caption("Powered by FastAPI and Streamlit")
