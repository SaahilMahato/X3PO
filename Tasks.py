import Assistant
import alsaaudio
import subprocess
import pytube
from pytube.exceptions import RegexMatchError


class OpenApp(Assistant.Interact):
    def __init__(self):
        super().__init__()
        self.app_dictionary = {
            "vscode": "code",
            "vs code": "code",
            "visual studio code": "code",
            "chromium": "chromium-browser",
            "geany": "geany"
        }

    def open(self, app):
        try:
            subprocess.call(self.app_dictionary[app])
        except ...:
            self.speak("Sorry, the application is not installed")


class SystemControl(Assistant.Interact):
    def __init__(self):
        super().__init__()
        self.audio_mixer = alsaaudio.Mixer()
        self.volume_value = None
        self.brightness_value = None

    def change_volume(self, value):
        try:
            assert 0 <= value <= 100
            self.audio_mixer.setvolume(value)
        except ...:
            self.speak("Please install alsa audio to enable this command")

    def mute_audio(self):
        try:
            self.audio_mixer.setvolume(0)
        except ...:
            self.speak("Please install alsa audio to enable this command")


class VideoDownload(Assistant.Interact):
    def __init__(self):
        super().__init__()

    def download_video(self):
        try:
            self.get_textbox_input("Enter the video URL and press Enter.")
            yt = pytube.YouTube(self.text_box_input)
            video = yt.streams.first()
            self.speak(f"Downloading video {yt.title}.")
            video.download(self.youtube_download_path)
            self.speak(f"Download complete.")
        except RegexMatchError:
            self.speak("Sorry, incorrect url.")
        except ConnectionError:
            self.speak("Sorry, no internet connection.")
        except ...:
            self.speak("Sorry, an error occurred.")


if __name__ == "__main__":
    VideoDownload().download_video()
