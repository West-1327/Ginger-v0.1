import datetime
from text_to_voice import say_something


# Create a function that says the specific time
def the_time(text):
    time_stamp = datetime.datetime.now().strftime("%I:%M:%S")
    if "the time" in text:
        s = say_something("The time is")
        l = say_something(time_stamp)
        return s, l
    else:
        return False

# Create a function that says the specific date


def the_date(text):
    if "the date" in text:
        # tells the date
        day = int(datetime.datetime.now().day)
        month = datetime.datetime.now()
        year = int(datetime.datetime.now().year)
        # say day
        l = say_something("it's the")
        m = say_something(day)
        # says the month
        n = say_something("of the month")
        o = say_something(month.strftime("%B"))
        # says the year
        p = say_something("of the year ")
        q = say_something(year)
        return l, m, n, o, p, q
    else:
        return False
