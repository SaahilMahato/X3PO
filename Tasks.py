import os
import Assistant
import alsaaudio
import tkinter as tk
import re
import subprocess
import pytube
from pytube.exceptions import RegexMatchError


class OpenApp(Assistant.Interact):
    def __init__(self, user_input):
        super().__init__()
        self.app_dictionary = {
            "vscode": "code",
            "vs code": "code",
            "visual studio code": "code",
            "chromium": "chromium-browser",
            "geany": "geany",
            "android studio": "/home/saahil/android-studio/bin/studio.sh"
        }
        self.user_input = user_input

    def open(self):
        try:
            subprocess.call(self.app_dictionary[self.user_input])
        except:
            self.speak("Sorry, the application is not installed")


class SystemControl(Assistant.Interact):
    def __init__(self, volume_value=0):
        super().__init__()
        self.audio_mixer = alsaaudio.Mixer()
        self.volume_value = volume_value

    def change_volume(self):
        try:
            assert 0 <= self.volume_value <= 100
            self.audio_mixer.setvolume(self.volume_value)
        except:
            self.speak("Please install alsa audio to enable this command")

    def mute_audio(self):
        try:
            self.audio_mixer.setvolume(0)
        except:
            self.speak("Please install alsa audio to enable this command")


class VideoDownload(Assistant.Interact):
    def __init__(self):
        super().__init__()
        self.root = tk.Tk()
        self.text_box = tk.Text(self.root, height=1, width=60)
        self.text_box_input = None
        self.done_button = tk.Button(self.root, text="Done", command=self.set_user_input)
        self.youtube_download_path = "/home/saahil/Videos"

    def set_user_input(self):
        self.text_box_input = self.text_box.get("1.0", 'end-1c')
        self.root.destroy()

    def get_user_input(self):
        self.root.title("Enter video url")
        self.text_box.pack()
        self.done_button.pack()
        tk.mainloop()

    def download_video(self):
        try:
            self.get_user_input()
            yt = pytube.YouTube(self.text_box_input)
            video = yt.streams.first()
            self.speak(f"Downloading video {yt.title}.")
            video.download(self.youtube_download_path)
            self.speak(f"Download complete.")
        except RegexMatchError:
            self.speak("Sorry, incorrect url.")
        except ConnectionError:
            self.speak("Sorry, no internet connection.")
        except:
            self.speak("Sorry, pytube need to be updated.")


class CreateProject(Assistant.Interact):
    def __init__(self):
        super().__init__()
        self.root = tk.Tk()
        self.project_name_text_box = tk.Text(self.root, height=1, width=30)
        self.project_files_name_text_box = tk.Text(self.root, height=1, width=80)
        self.remote_url_text_box = tk.Text(self.root, height=1, width=80)
        self.project_name_text_box_input = None
        self.project_files_name_text_box_input = None
        self.remote_url_text_box_input = None
        self.done_button = tk.Button(self.root, text="Done", command=self.set_user_input)
        self.project_path = "/home/saahil/"

    def set_user_input(self):
        self.project_name_text_box_input = self.project_name_text_box.get("1.0", 'end-1c')
        self.project_files_name_text_box_input = self.project_files_name_text_box.get("1.0", 'end-1c')
        self.remote_url_text_box_input = self.remote_url_text_box.get("1.0", 'end-1c')
        self.root.destroy()

    def get_user_input(self):
        self.root.title("Enter project name and git url")
        self.project_name_text_box.pack()
        self.project_files_name_text_box.pack()
        self.remote_url_text_box.pack()
        self.done_button.pack()
        tk.mainloop()

    def create_project(self):
        try:
            self.get_user_input()
            assert self.project_name_text_box_input
            assert re.match('((git|ssh|http(s)?)|(git@[\w\.]+))(:(//)?)([\w\.@\:/\-~]+)(\.git)(/)?', self.remote_url_text_box_input)
            os.system(f'mkdir {self.project_path}{self.project_name_text_box_input}')
            os.chdir(f'{self.project_path}{self.project_name_text_box_input}')
            os.system('git init')
            os.system('git config --global user.name "SaahilMahato"')
            os.system('git config --global user.email "saahilmahato72@gmail.com"')
            os.system(f'git remote add origin {self.remote_url_text_box_input}')
            for file in self.project_files_name_text_box_input.split(","): os.system(f"touch {file}")
        except AssertionError:
            self.speak("Sorry, invalid git URL or project name")
        except:
            self.speak("Sorry, an error occurred")
