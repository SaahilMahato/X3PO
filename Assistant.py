import pyttsx3
import speech_recognition as sr
import tkinter as tk


class Character:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self.engine.setProperty('rate', 130)
        self.root = tk.Tk()
        self.text_box = None
        self.text_box_input = None
        self.done_button = None
        self.youtube_download_path = "/home/saahil/Videos"


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
            except ...:
                self.speak("Sorry I couldn't get what you said")

    def set_textbox_input(self):
        self.text_box_input = self.text_box.get("1.0", 'end-1c')
        self.root.destroy()

    def get_textbox_input(self, title):
        self.root.title(title)
        self.text_box = tk.Text(self.root, height=1, width=40)
        self.done_button = tk.Button(self.root, text="Done", command=self.set_textbox_input)
        self.text_box.pack()
        self.done_button.pack()
        tk.mainloop()


if __name__ == "__main__":
    pass
