# say_voice.py

import pyttsx3


def say(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()
