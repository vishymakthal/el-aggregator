import praw
from creds import CREDENTIALS
import re
import sys
import random

reddit = praw.Reddit(client_id=CREDENTIALS.client_id,
                    client_secret=CREDENTIALS.client_secret,
                    user_agent=CREDENTIALS.user_agent,
                    )

def searchSubreddit(query):
    '''
    Calls upon the reddit API instance to search by the term passed in. Populates
    the global playerHighlights list.

    Args:
        string query: The query to pass to the reddit search function.  

    Returns:
        list[dict] playerHighlights: list of highlight key-value pairs
    '''
    print(query)
    player_highlights = []
    for post in reddit.subreddit('soccer').search('{} flair:media'.format(query),sort="new", limit=25):
        if re.search('\[[0-9]+\]|[0-9]{1,2}\'',post.title):
            player_highlights.append({'title' : post.title, 'link' : post.url})

    if not player_highlights:
        return [{'title': 'No Highlights Found on Reddit!', 'link' : ''}]
    return player_highlights

def searchHighlightsByPlayer(player, club):
    '''
    Searches /r/soccer for video clip links containing a player's name. Posts are filtered
    with the flair "media" so that highlights are queried.

    Args:
        string player: Player name to search
        string club: Club name to include in the query alongside player name

    Returns:
        set playerHighlights: list of highlights in key-value form ( {title : link} )

    '''

    return searchSubreddit(player + ' ' + club) #search the subreddit by full name of player

if __name__ == '__main__':

    p = sys.argv[1]
    c = ' '.join(sys.argv[2:])
    print(searchHighlightsByPlayer(p,c))
    