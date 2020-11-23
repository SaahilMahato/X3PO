import Assistant
import alsaaudio


class SystemControl(Assistant.Interact):
    def __init__(self, volume_value=0):
        super().__init__()
        self.audio_mixer = alsaaudio.Mixer()
        self.volume_value = volume_value

    def change_volume(self):
        try:
            assert 0 <= self.volume_value <= 100
            self.audio_mixer.setvolume(self.volume_value)
            self.speak("Volume changed.")
        except:
            self.speak("Please install alsa audio to enable this command")

    def mute_audio(self):
        try:
            self.audio_mixer.setvolume(0)
            self.speak("Audio muted.")
        except:
            self.speak("Please install alsa audio to enable this command")