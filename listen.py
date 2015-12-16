#!/usr/bin/python

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
api_keys = None
with open('./keys', 'r') as file:
    api_keys = [line.strip('\n') for line in file]

def do_recognize(recognizer, audio, key, use_wit):
    phrase = ""
    engine = ""
    print('use wit: ' + str(use_wit))
    print('using key: ' + key)
    if use_wit:
        # recognize speech using Wit.ai
        WIT_AI_KEY = "AVPNCOC732URGDUWILQ333FQLWJZBZON" # Wit.ai keys are 32-character uppercase alphanumeric strings
        phrase = r.recognize_wit(audio, key=WIT_AI_KEY)
        engine = "Wit.ai"

    else:
        # received audio data, now we'll recognize it using Google Speech Recognition
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        if key:
            print('using custom key')
            recognizer.recognize_google(audio, key)
        else:
            print('using built in api key')
            recognizer.recognize_google(audio)

        phrase = recognizer.recognize_google(audio)
        engine = "Google Speech Recognition"

    print(engine + " thinks you said: " + phrase)
    return phrase

def read_key():
    return api_keys[1]

def write_key(key):
    print('writing key: ' + key)
    with open('./currkey', 'w') as keyfile:
        keyfile.write(key)

def keychange():
    key = api_keys.pop(1)
    api_keys.append(key)
    return api_keys[1]

# this is called from the background thread
def callback(recognizer, audio):
    key = read_key()

    use_wit = key == 'wit'

    retries = 3
    try:
        retries -= 1
        phrase = do_recognize(recognizer, audio, key, use_wit)

        with open('/home/ubuntu/chatbotio', 'w') as botcomm:
            botcomm.write(phrase)

    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print("Could not request results from service; {0}".format(e))
        if not use_wit:
            print("going to try changing keys")
            key = keychange(key)
            if key == 'wit':
                print('falling back to wit')


r = sr.Recognizer()
#r.pause_threshold = 1.0 # seconds of pause to end a phrase.
#r.phrase_threshold = 0.4 # seconds of speech time before phrase can be considered started

m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source) # we only need to calibrate once, before we start listening

print('using energy threshold: ' + str(r.energy_threshold))
# start listening in the background (note that we don't have to do this inside a `with` statement)
stop_listening = r.listen_in_background(m, callback)
# `stop_listening` is now a function that, when called, stops background listening

# do some other computation for 5 seconds, then stop listening and keep doing other computations
import time
getinput = raw_input or input
while True:
    cmd = getinput('> ').lower()
    if (cmd == 'quit' or cmd == 'exit'):
        print('exiting')
        stop_listening()
        exit()
