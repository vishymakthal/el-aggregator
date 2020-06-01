import wikipedia

def get_bio(player_name, short_name):
    try:
        bio = wikipedia.summary(player_name)
    except wikipedia.exceptions.PageError:
        try:
            bio = wikipedia.summary(short_name)
        except wikipedia.exceptions.PageError:
            return "No wikipedia entry found."

    return bio 