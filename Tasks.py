import os
import Assistant


class OpenApp(Assistant.Interact):
    def __init__(self):
        super().__init__()
        self.app_dictionary = {
            "pycharm": "pycharm",
            "vscode": "code",
            "vs code": "code",
            "visual studio code": "code",
            "chromium": "chromium-browser",
            "geany": "geany",
            "android studio": "android-studio"
        }

    def open(self):
        app_text = self.listen().lower()
        assert app_text is not None
        try:
            os.system(self.app_dictionary[app_text])
        except:
            self.speak("Sorry, the application is not installed")

"""
class SystemControl(Assistant.Interact):
    def __init__(self):
        super().__init__()
        self.volume_value = None
        self.brightness_value = None

    def change_volume(self):
        




if __name__ == "__main__":
    OpenApp().open()
"""