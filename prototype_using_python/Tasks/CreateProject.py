import Assistant
import tkinter as tk
import re
import os

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
            self.speak("Project Created.")
        except AssertionError:
            self.speak("Sorry, invalid git URL or project name")
        except:
            self.speak("Sorry, an error occurred")