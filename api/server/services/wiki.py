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

def get_url(player_name, short_name):
    try:
        return wikipedia.page(player_name).url
    except wikipedia.exceptions.PageError:
        try:
            return wikipedia.page(short_name).url
        except wikipedia.exceptions.PageError:
            return ''
