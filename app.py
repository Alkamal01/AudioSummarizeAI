import streamlit as st
from pydub import AudioSegment
import tempfile
import os
import google.generativeai as genai
import yt_dlp
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

last_status = None 


def summarize_audio(audio_file_path):
    """Summarize the audio using Google's Generative API."""
    st.info("Generating summary...")
    model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
    audio_file = genai.upload_file(path=audio_file_path)
    response = model.generate_content(
        [
            "Please summarize the following audio.",
            audio_file
        ]
    )
    return response.text


def save_uploaded_file(uploaded_file):
    """Save uploaded file to a temporary file and return the path."""
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.' + uploaded_file.name.split('.')[-1]) as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            return tmp_file.name
    except Exception as e:
        st.error(f"Error handling uploaded file: {e}")
        return None


def youtube_download_hook(d):
    """Progress hook for YouTube download."""
    global last_status  
    if d['status'] == 'downloading' and last_status != 'downloading':
        st.info("Downloading video...")
        last_status = 'downloading'
    elif d['status'] == 'finished' and last_status != 'finished':
        st.info("Download complete. Extracting audio...")
        last_status = 'finished'


def download_audio_from_youtube(youtube_url):
    """Download audio from a YouTube video using yt_dlp and return the file path."""
    try:
        temp_dir = tempfile.mkdtemp()
        audio_file_base = os.path.join(temp_dir, "youtube_audio")  

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': audio_file_base, 
            'postprocessors': [
                {
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }
            ],
            'quiet': True, 
            'progress_hooks': [youtube_download_hook],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])

        processed_audio_file = f"{audio_file_base}.mp3"

        if os.path.exists(processed_audio_file):
            return processed_audio_file
        else:
            raise FileNotFoundError("The expected audio file was not created.")

    except Exception as e:
        st.error(f"Error downloading audio from YouTube: {e}")
        return None


# Streamlit app interface
st.title('🎵AudioSummarizeAI🎙️')

with st.expander("About this app"):
    st.write("""
        This app uses Google's generative AI to summarize audio files or YouTube videos. 
        Upload your audio file or provide a YouTube link to get a concise summary of its content.
    """)

tab1, tab2 = st.tabs(["Upload Audio File", "YouTube Link"])

with tab1:
    audio_file = st.file_uploader("Upload Audio File", type=['wav', 'mp3'])
    if audio_file is not None:
        audio_path = save_uploaded_file(audio_file) 
        st.audio(audio_path)

        if st.button('Summarize Audio', key="summarize_audio"):
            with st.spinner('Summarizing...'):
                summary_text = summarize_audio(audio_path)
                st.info(summary_text)

with tab2:
    youtube_url = st.text_input("Enter YouTube Link")
    if youtube_url:
        if st.button('Download and Summarize Audio', key="youtube_summarize"):
            with st.spinner('Processing YouTube video...'):
                audio_path = download_audio_from_youtube(youtube_url)
                if audio_path:
                    summary_text = summarize_audio(audio_path)
                    st.info(summary_text)

st.markdown(
    """
    <hr>
    <div style="text-align: center;">
        <p>Built with ❤️ by <strong>kaftandev🥷</strong></p>
        <a href="https://github.com/Alkamal01" target="_blank">
            <img src="https://img.icons8.com/material-outlined/24/github.png" alt="GitHub">
        </a>
        <a href="https://twitter.com/kaftandev" target="_blank">
            <img src="https://img.icons8.com/material-outlined/24/twitter.png" alt="Twitter">
        </a>
        <a href="https://linkedin.com/in/alkamal" target="_blank">
            <img src="https://img.icons8.com/material-outlined/24/linkedin.png" alt="LinkedIn">
        </a>
        <br>
        <br>
        <a href="https://www.buymeacoffee.com/kaftandev" target="_blank">
            <img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=kaftandev&button_colour=FFDD00&font_colour=000000&font_family=Arial&outline_colour=000000&coffee_colour=ffffff" alt="Buy Me a Coffee">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
