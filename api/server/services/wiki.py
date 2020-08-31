import wikipedia

def get_bio(player_name, short_name):
    try:
        bio = wikipedia.summary(player_name, sentences=1)
    except wikipedia.exceptions.PageError:
        try:
            bio = wikipedia.summary(short_name, sentences=1)
        except wikipedia.exceptions.PageError:
            return "No wikipedia entry found."

    return bio 