from chatterbot import ChatBot

chatbot = ChatBot("HAL 9000")
chatbot.train("chatterbot.corpus.english")

while True:
    message = raw_input("> ")

    if "exit" in message:
        print("Well that's rude.  Goodbye")
        exit()

    chatbot.get_response(message)

