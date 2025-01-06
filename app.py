import streamlit as st
from pydub import AudioSegment
import tempfile
import os
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

# Configure Google API for audio summarization
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

def summarize_audio(audio_file_path):
    """Summarize the audio using Google's Generative API."""
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

# Streamlit app interface
st.title('AudioSummarizeAI')

with st.expander("About this app"):
    st.write("""
        This app uses Google's generative AI to summarize audio files. 
        Upload your audio file in WAV or MP3 format and get a concise summary of its content.
    """)

audio_file = st.file_uploader("Upload Audio File", type=['wav', 'mp3'])
if audio_file is not None:
    audio_path = save_uploaded_file(audio_file)  # Save the uploaded file and get the path
    st.audio(audio_path)

    if st.button('Summarize Audio'):
        with st.spinner('Summarizing...'):
            summary_text = summarize_audio(audio_path)
            st.info(summary_text)
# Footer Section
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
