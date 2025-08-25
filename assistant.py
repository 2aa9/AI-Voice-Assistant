
### `assistant.py`
```python
import speech_recognition as sr
import pyttsx3
import webbrowser

engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio).lower()
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            return ""

if __name__ == "__main__":
    speak("Hello! How can I help you?")
    while True:
        command = listen()
        if "open youtube" in command:
            webbrowser.open("https://youtube.com")
            speak("Opening YouTube")
        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            break
        elif command:
            speak(f"You said: {command}")
