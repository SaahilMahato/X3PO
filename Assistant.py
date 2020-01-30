import pyttsx3
import speech_recognition as sr


class Character:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self.engine.setProperty('rate', 130)


class Interact(Character):
    def __init__(self):
        super().__init__()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with sr.Microphone() as source:
            audio = self.recognizer.listen(source)
            try:
                temp_text = self.recognizer.recognize_google(audio)
                return temp_text
            except:
                pass
