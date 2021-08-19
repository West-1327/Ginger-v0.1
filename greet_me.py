import datetime
from text_to_voice import say_something


# AI greeting
# if Hello or West or afternoon or evening is text:
def greeting(text):
    time = datetime.datetime.now().hour
    if 5 < time < 12:
        greeting_condition = ["hello", "hey", "ginger", "morning", "buddy"]
        for i in range(len(text)):
            word = greeting_condition[i]
            if word[i] in text:
                m = say_something("Good morning sir, i hope you slept well")
                return m
            else:
                pass
    # Afternoon Greeting
    elif 12 < time < 18:
        greeting_condition = ["hello", "hey", "ginger", "afternoon", "buddy"]
        for i in range(len(text)):
            word = greeting_condition[i]
            if word[i] in text:
                a = say_something("Good Afternoon Sir, i hope your enjoying your day")
                return a
            else:
                pass
    elif 18 < time < 24:
        greeting_condition = ["hello", "hey", "ginger", "evening", "buddy"]
        for i in range(len(text)):
            word = greeting_condition[i]
            if word[i] in text:
                e = say_something("Good Evening Sir")
                return e
            else:
                pass

    # After midnight
    else:
        greeting_condition = ["hello", "hey", "ginger", "evening", "buddy"]
        for i in range(len(text)):
            word = greeting_condition[i]
            if word[i] in text:
                k = say_something("Sir,  aren't you supposed to be asleep?")
                return k
            else:
                pass

