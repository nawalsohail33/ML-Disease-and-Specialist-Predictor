# voice.py
import speech_recognition as sr
import pyttsx3

def speak_output(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_symptoms_from_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak_output("Please describe your symptoms...")  # ✅ This only runs when called
        print("Please describe your symptoms...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        symptoms_text = recognizer.recognize_google(audio)
        speak_output(f"You said: {symptoms_text}")
        return symptoms_text
    except sr.UnknownValueError:
        speak_output("Sorry, I could not understand the audio.")
        return None
    except sr.RequestError:
        speak_output("Network error. Please check your internet connection.")
        return None
