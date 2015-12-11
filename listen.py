#!/usr/bin/python

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

def do_recognize(recognizer, audio, key, use_wit):
    phrase = ""
    engine = ""
    print('use wit: ' + use_wit)
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
        if key is None:
            print('using built in api key')
            recognizer.recognize_google(audio)
        else:
            print('using custom key')
            recognizer.recognize_google(audio, key)

        phrase = recognizer.recognize_google(audio)
        engine = "Google Speech Recognition"

    print(engine + " thinks you said: " + phrase)
    return phrase

def read_key():
    key = None
    with open('./currkey', 'r') as keyfile:

        key = keyfile.readline()
        if key is not None:
            key = key.strip('\n')

    print('got current key: ' + key)
    return key

def write_key(key):
    print('writing key: ' + key)
    with open('./currkey', 'w') as keyfile:
        keyfile.write(key)

def keychange(last_key):
    keys = None
    with open('./keys', 'r') as file:
        keys = [line.strip('\n') for line in file]

    print('found ' + len(keys) + ' keys in keyfile')

    key_index = None
    if last_key in keys:
        key_index = keys.index(last_key)
    next_key = 'wit'
    if key_index is not None and key_index < len(keys):
        next_key = keys[key_index+1]

    write_key(next_key)

    return next_key

# this is called from the background thread
def callback(recognizer, audio):
    key = read_key()

    use_wit = key == 'wit'

    retries = 3
    while retries > 0:
        try:
            retries -= 1
            return do_recognize(recognizer, audio, key, use_wit)

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
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source) # we only need to calibrate once, before we start listening

# start listening in the background (note that we don't have to do this inside a `with` statement)
stop_listening = r.listen_in_background(m, callback)
# `stop_listening` is now a function that, when called, stops background listening

# do some other computation for 5 seconds, then stop listening and keep doing other computations
import time
running = True
getinput = raw_input or input
while running:
    cmd = getinput().lower()
    if (cmd == 'quit' or cmd == 'exit'):
        print('exiting')
        stop_listening()
        running = False
