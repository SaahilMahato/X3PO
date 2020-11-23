import Assistant
import subprocess


class OpenApp(Assistant.Interact):
    def __init__(self, user_input):
        super().__init__()
        self.app_dictionary = {
            "vscode": "code",
            "vs code": "code",
            "visual studio code": "code",
            "code": "code",
            "chromium": "chromium-browser",
            "geany": "geany",
            "android studio": "/home/saahil/android-studio/bin/studio.sh",
            "simple note": "simplenote"
        }
        self.user_input = user_input

    def open(self):
        try:
            subprocess.call(self.app_dictionary[self.user_input])
            self.speak("Application started.")
        except:
            self.speak("Sorry, the application is not installed")