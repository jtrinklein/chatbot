from chatterbot import ChatBot

chatbot = ChatBot("HAL 9000")
chatbot.train("chatterbot.corpus.english")

while True:
    try:
        message = raw_input("> ")
        if "exit" in message:
            print("Well that's rude.  Goodbye")
            exit()
        else:
            chatbot.get_response(message)
    except EOFError as e:
        print("got eof")
