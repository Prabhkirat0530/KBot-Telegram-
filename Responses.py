from datetime import datetime


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "hey", "yo",):
        return "Hey! What's up?"

    if user_message in ("who are you", "who are you?",):
        return "I am KBot"

    if user_message in ("who created you", "why you are created?"):
        return "I am created to help you out"

    if user_message in ("time", "time?","date", "date?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)

    return "I don't know what you said."
