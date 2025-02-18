import streamlit as st
from gtts import gTTS
import os
import time  # For simulating the time delay
from langid import classify  # For detecting language of input text

# Set page config with title and favicon
st.set_page_config(page_title="Multi-Language Text to Speech", page_icon="🌍")

# Supported Languages
languages = {
    "English": "en",
    "Tamil": "ta",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Hindi": "hi",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese (Mandarin)": "zh-cn",
    "Russian": "ru",
    "Arabic": "ar"
}

# App Title
st.title("🌍 Multi-Language Text to Speech")
st.write("Convert text into speech in multiple languages with native speaker accents!")

# Language Selection
language = st.selectbox("Choose Language:", list(languages.keys()))

# Text Input
text = st.text_area("Enter Text:", placeholder="Type something...")

# Function to check if input language matches selected language
def check_language(text, selected_language):
    # Detect the language of the input text
    detected_lang = classify(text)[0]  # Get the detected language
    selected_lang_code = languages[selected_language]
    
    if detected_lang != selected_lang_code:
        return False
    return True

# Convert Text to Speech
if st.button("Convert to Speech"):
    if text:
        if check_language(text, language):  # Check if input language matches the selected language
            with st.spinner("Converting text to speech..."):
                # Simulate some delay (you can remove this in the actual app)
                time.sleep(2)  # Simulated delay to show spinner
                
                # Convert to speech
                lang_code = languages[language]
                speech = gTTS(text=text, lang=lang_code)
                speech.save("audio.mp3")

                # Audio playback
                audio_file = open("audio.mp3", "rb")
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format='audio/mp3')
                
                # Option to Download Audio
                st.download_button(label="Download Audio", data=audio_bytes, file_name='audio.mp3', mime='audio/mp3')
        else:
            st.warning(f"The input text is not in the selected language ({language}). Please enter text in {language}.")
    else:
        st.warning("Please enter some text to convert.")

# Footer Section
st.markdown("""
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #f1f1f1;
            text-align: center;
            padding: 10px 0;
            font-size: 14px;
            color: #555;
        }
    </style>
    <div class="footer">
        <p>Made with ❤️ by Dhanashree S R | Multi-Language Text to Speech</p>
    </div>
""", unsafe_allow_html=True)