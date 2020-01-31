import Assistant
import DeduceInput

if __name__ == '__main__':
    trigger_word = "hello"
    x3po = Assistant.Interact()
    while True:
        user_input_trigger = x3po.listen()
        if user_input_trigger == "hello":
            x3po.speak("Hi, How can I help you?")
            user_query = x3po.listen()
            if user_query is not None:
                DeduceInput.DeduceInput(user_query).deduce()
            else:
                x3po.speak("Sorry, I could not get you.")
