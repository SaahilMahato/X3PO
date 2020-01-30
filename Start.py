import Assistant
import DeduceInput

if __name__ == '__main__':
    trigger_word = "hello"
    while True:
        user_input_trigger = Assistant.Interact().listen()
        if user_input_trigger == "hello":
            Assistant.Interact().speak("Hi, How can I help you?")
            user_query = Assistant.Interact().listen()
            if user_query is not None:
                DeduceInput.DeduceInput(user_query).deduce()
            else:
                Assistant.Interact().speak("Sorry, I could not get you.")
        else:
            continue
