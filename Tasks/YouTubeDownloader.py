import Assistant
import pytube
import tkinter as tk
from pytube.exceptions import RegexMatchError


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
            self.speak("Sorry, pytube needs to be updated.")
