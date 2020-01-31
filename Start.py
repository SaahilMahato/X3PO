import Assistant
import DeduceInput


class Start(Assistant.Interact):
    def __init__(self):
        super().__init__()
        self.trigger_word = "hello"
        self.shut_down_word = "goodbye"

    def start(self):
        while True:
            user_input_trigger = self.listen()
            if user_input_trigger == self.shut_down_word:
                self.speak("I am shutting down.")
                exit()
            if user_input_trigger == self.trigger_word:
                self.speak("Hi, How can I help you?")
                user_query = self.listen()
                if user_query is not None:
                    DeduceInput.DeduceInput(user_query).deduce()
                else:
                    self.speak("Sorry, I could not get you.")


if __name__ == '__main__':
    Start().start()
