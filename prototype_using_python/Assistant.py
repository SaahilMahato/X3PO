import pyttsx3
import speech_recognition as sr
import pygame


class UserInterface:
    def __init__(self):
        pygame.init()
        self.height = 600
        self.width = 800
        self.window_size = (self.width, self.height)
        self.white_color = (255, 255, 255)
        self.black_color = (0, 0, 0)
        self.screen = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("X-3PO")
        self.VA_img = pygame.image.load('Img/VA.png')
        self.game_exit = False
        self.text = ""
        self.reply = ""
        self.game_run = True
        self.display()

    def message(self, msg, color, x, y, font):
        font = pygame.font.SysFont(None, font)
        screen_text = font.render(msg, True, color)
        self.screen.blit(screen_text, [x, y])

    def display(self):
        self.screen.fill(self.white_color)
        self.screen.blit(self.VA_img, ((self.width // 2) - 170, (self.height // 2) - 300))
        self.message("X-3PO", self.black_color, 330, 350, 70)
        self.message(self.text, self.black_color, 300, 420, 50)
        self.message(self.reply, self.black_color, 300, 480, 60)
        pygame.display.update()


class Interact(UserInterface):
    def __init__(self):
        super().__init__()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 130)
        self.audio = None
        self.temp_text = None
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def speak(self, text):
        self.reply = text
        self.display()
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            self.audio = self.recognizer.listen(source)
            try:
                self.temp_text = self.recognizer.recognize_google(self.audio)
                self.reply = self.temp_text
                self.display()
                return self.temp_text
            except:
                pass


if __name__ == '__main__':
    a = Interact()
