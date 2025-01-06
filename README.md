# AudioSummarizeAI

**AudioSummarizeAI** is a simple yet powerful application that uses Google's Generative AI to summarize audio files. Whether it's a lecture, podcast, or meeting recording, this app will provide you with a concise summary of the content.

## Features
- Upload audio files in **WAV** or **MP3** format.
- Summarize audio content using Google's advanced **Generative AI**.
- Clean, intuitive user interface powered by **Streamlit**.

## How It Works
1. **Upload Audio**: Upload an audio file (WAV or MP3 format).
2. **Summarize**: Click the "Summarize Audio" button to get a concise summary of the content.
3. **View Results**: The app generates a summary and displays it directly in the interface.

## Built With
- **[Streamlit](https://streamlit.io/)**: For building an interactive web app.
- **[Pydub](https://github.com/jiaaro/pydub)**: For audio file handling.
- **[Google Generative AI](https://cloud.google.com/)**: For AI-powered audio summarization.
- **[dotenv](https://pypi.org/project/python-dotenv/)**: For managing environment variables.

## Installation

### Prerequisites
- Python 3.8 or higher
- A Google Generative AI API key ([Sign up here](https://cloud.google.com/)).

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/alkamal01/AudioSummarizeAI.git
   cd AudioSummarizeAI

2. Create a virtual environment:
    ```bash 
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate

3. Install dependencies:
    ```bash
    pip install -r requirements.txt

4. Set up your environment:
    Create a .env file in the project root.
    Add your Google API key:
    ```bash
    GOOGLE_API_KEY=your_api_key_here

5. Run the app:
    ```bash 
    streamlit run app.py

### USAGE

1. Open the app in your browser at http://localhost:8501.
2. Upload your audio file and wait for the summarization process.
3. View the generated summary.

### Screenshots

### Upload Audio File

### Summary Output

### Contributing

Contributions are welcome! To contribute:

1. Fork the repository.

2. Create a feature branch:
    ```bash
    git checkout -b feature-name

3. Commit your changes:
    ```bash
    git commit -m "Add your message here"

4. Push to your branch:
    ```bash
    git push origin feature-name

5. Create a pull request.

### License

This project is licensed under the MIT License - see the LICENSE file for details.

### Author

Kamal Aliyu

### Acknowledgments

Thanks to Streamlit for making app development easy.
Special thanks to Google for their Generative AI API.
Built with ❤️ by Kamal Aliyu.
