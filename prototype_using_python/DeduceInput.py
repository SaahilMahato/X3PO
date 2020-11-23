from Tasks import OpenApp
from Tasks import SystemControl
from Tasks import YouTubeDownloader
from Tasks import CreateProject
import Assistant
import pygame


class DeduceInput(Assistant.Interact):
    def __init__(self, user_input):
        super().__init__()
        self.user_input = user_input

    def deduce(self):
        if "open" in self.user_input:
            app = self.user_input[5:]
            OpenApp.OpenApp(app).open()
        elif "volume" in self.user_input:
            volume_value = int(self.user_input[-3:])
            SystemControl.SystemControl(volume_value).change_volume()
        elif "mute" in self.user_input:
            SystemControl.SystemControl().mute_audio()
        elif "download video" in self.user_input:
            YouTubeDownloader.VideoDownload().download_video()
        elif "create project" in self.user_input:
            CreateProject.CreateProject().create_project()
        elif "shutdown" in self.user_input:
            pygame.display.quit()
            quit()
        else:
            self.speak("Sorry, I could not understand you.")
