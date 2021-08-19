from voice_to_text import get_audio
from greet_me import greeting
from Power_down import shutdown, re_boot, shut_down
from Power_down import restart
from date_and_time import the_date
from date_and_time import the_time
from text_to_voice import say_something

said = get_audio()


def main(text):

    if "you up" in text:
        say_something(" for you sir,  always")

    # restart condition
    elif "restart" in text:
        restart(re_boot)
    # shutdown protocol
    elif text:
        the_time(text)
        the_date(text)
        greeting(text)

    elif text:
        shut_down_protocol = ["shut down", "shutdown", "kill power", "killpower"]
        for i in range(len(text)):
            word = shut_down_protocol
            i = 0
            if word[i] not in text:
                pass
            else:
                say_something("initiating shutdown sequence, Peace Out")
                shutdown(shut_down)
                break


while said == "":
    say_something("I didn't get that please repeat")
    said = get_audio()

main(said)
