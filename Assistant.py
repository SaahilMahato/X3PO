import pyttsx3
import speech_recognition as sr


class Interact:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 130)
        self.audio = None
        self.temp_text = None
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            self.audio = self.recognizer.listen(source)
            try:
                self.temp_text = self.recognizer.recognize_google(self.audio)
                return self.temp_text
            except:
                pass
