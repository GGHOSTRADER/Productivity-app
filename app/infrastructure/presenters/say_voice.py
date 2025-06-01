# say_voice.py

import pyttsx3


def say(message):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)  # Default is ~200. Lower = slower.
    engine.say(message)
    engine.runAndWait()
