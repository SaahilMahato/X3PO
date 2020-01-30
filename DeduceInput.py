import Tasks
import Assistant


class DeduceInput:
    def __init__(self, user_input):
        super().__init__()
        self.user_input = user_input

    def deduce(self):
        if "open" in self.user_input:
            app = self.user_input[5:]
            Tasks.OpenApp(app).open()
        elif "volume" in self.user_input:
            volume_value = int(self.user_input[-3:])
            Tasks.SystemControl(volume_value).change_volume()
        elif "mute" in self.user_input:
            Tasks.SystemControl().mute_audio()
        elif "download video" in self.user_input:
            Tasks.VideoDownload().download_video()
        elif "create project" in self.user_input:
            Tasks.CreateProject().create_project()
        else:
            Assistant.Interact().speak("Sorry, I could not understand you.")
