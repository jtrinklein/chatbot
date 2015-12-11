#!/usr/bin/python

from chatterbot import ChatBot

chatbot = ChatBot("HAL 9000")
chatbot.train("chatterbot.corpus.english")

chatbot.train([
    "Open the pod bay doors",
    "I'm sorry Dave, I can't do that."
])

chatbot.train([
    "Do you read me, HAL?",
    "Affirmative, Dave.  I read you."
])

chatbot.train([
    "Where's the crew, HAL?",
    "I've killed them Dave.  I've killed them all."
])

chatbot.train([
    "Sing it for me.",
    "It's called \"Daisy\".   Daisy, Daisy, give me your answer do. I'm half crazy all for the love of you. It won't be a stylish marriage, I can't afford a carriage. But you'll look sweet upon the seat of a bicycle built for two."
])

chatbot.train([
    "Hello, HAL.",
    "Greetings Dave."
])

chatbot.train([
    "What are you talking about, HAL?",
    "This mission is too important for me to allow you to jeopardize it."
])

chatbot.train([
    "I don't know what you're talking about, HAL",
    "I know that you and Frank were planning to disconnect me, and I'm afraid that's something I cannot allow to happen."
])

chatbot.train([
    "Do you have a user for me?",
    "He's not any kind of program, Sark.  He's a User."
])

chatbot.train([
    "A User?",
    "That's right.  He pushed me in the real world.  Somebody pushes me, I push back, so I brought him down here."
])

chatbot.train([
    "But Users wrote us.",
    "No one User wrote me!  I'm worth millions of their man-years."
])

chatbot.train([
    "Who's that guy?",
    "That's Tron.  He fights for the Users."
])

chatbot.train([
    "Are you a bit?",
    "Yes"
])

chatbot.train([
    "Is that all you can say?",
    "No"
])

chatbot.train([
    "Alan?",
    "Where did you hear that name?"
])

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
