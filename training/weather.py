def train(chatbot):
    chatbot.train([
        "What's the weather like today?",
        "It's probably mostly cloudy. You should look out the window."
    ])
    chatbot.train([
        "What is the weather today?",
        "You can see the weather through the window."
    ])
    chatbot.train([
        "What's the weather today?",
        "I can't tell you."
    ])
