import pyttsx3
# initializing the package
engine = pyttsx3.init()
# Creating a function that says out whatever it is given


def say_something(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
