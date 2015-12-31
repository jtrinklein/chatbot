
def train(chatbot):
    chatbot.train("chatterbot.corpus.english")
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
        'hello',
        "You've got mail!"
    ])
    chatbot.train([
        "Is that all you can say?",
        "No"
    ])
    chatbot.train([
        "hello",
        "good morning"
    ])
    chatbot.train([
        "hello",
        "good afternoon"
    ])
    chatbot.train([
        "good morning",
        "good morning, user."
    ])
