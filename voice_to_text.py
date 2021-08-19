import speech_recognition as sr


# takes audio converts to speech func
def get_audio():
    r = sr.Recognizer()  # recognizer object
    with sr.Microphone() as source:  # use mic to get audio
        audio = r.listen(source)  # use speech recognizer to listen to sound
        said = ""  # figure out what was said

    try:
        said = r.recognize_google(audio)  # use google api to recognize what we said
        print(said)
    except Exception as e:
        print("Exception: " + str(e))
    return said
