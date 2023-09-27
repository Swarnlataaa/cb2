import objc

import streamlit as st
import speech_recognition as sr
import pyttsx3

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as mic:
        st.write("Say something...")
        recognizer.adjust_for_ambient_noise(mic, duration=1)
        audio = recognizer.listen(mic)

    try:
        text = recognizer.recognize_google(audio)
        st.write("You said: " + text)
        return text
    except sr.UnknownValueError:
        st.write("I couldn't understand what you said.")
        return None
    except sr.RequestError as e:
        st.write("I encountered an error with the speech recognition service; {0}".format(e))
        return None

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    st.title("Speech Recognition Chatbot")

    user_input = st.text_area("You can type here:")

    if st.button("Speak"):
        user_input = speech_to_text()
        if user_input:
            text_to_speech("You said: " + user_input)

    if user_input:
        st.write("Chatbot response:")
        # Implement your chatbot logic here
        response = "I heard you say: " + user_input
        st.write(response)
        text_to_speech(response)

if __name__ == "__main__":
    main()
