import Assistant
import DeduceInput
from Tasks import FacialRecognition


class Start(Assistant.Interact):
    def __init__(self):
        super().__init__()
        self.trigger = ["Prajeet", "Saahil", "Saugat", "Aayush"]
        self.face = FacialRecognition.FacialRecognition()
        self.activate = False

    def start(self):
        trigger = self.face.recognize()
        while True:
            if trigger in self.trigger:
                self.text = f"Hello, {trigger}"
                self.display()
                trigger = None
                self.activate = True
                self.speak("How can I help you?")
            if self.activate:
                self.reply = "I am listening.."
                self.display()
                user_query = self.listen()
                if user_query is None:
                    continue
                else:
                    self.reply = user_query
                    self.display()
                    print(user_query)
                    DeduceInput.DeduceInput(user_query.lower()).deduce()


if __name__ == '__main__':
    Start().start()
