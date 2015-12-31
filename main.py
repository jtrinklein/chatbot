#!/usr/bin/python

from chatterbot import ChatBot
from training import base, hal, weather

chatbot = ChatBot("HAL 9000")
base.train(chatbot)
hal.train(chatbot)
weather.train(chatbot)

print('I am Alive!')

while True:
    try:
        message = ''
        with open('../../chatbotio', 'r') as input:
            message = input.read()
            if message:
                print('> ' + message)

        if "exit" in message:
            print("Well that's rude.  Goodbye")
            exit()
        else:
            response = chatbot.get_response(message)
            with open('../../sayio', 'w') as output:
                output.write(response)
    except EOFError as e:
        print("got eof")
