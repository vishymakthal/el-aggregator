import praw
import logging
import re

class Reddit():

    def __init__(self, client_id, client_secret, user_agent):
        self.reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

    def is_goal_to_post(self, title):
        return re.search('\[[0-9]+\]|[0-9]{1,2}\'', title)

    def search_subreddit(self, query):
        '''
        Calls the reddit API instance to search by the term passed in. Populates
        the global playerHighlights list.
        Args:
            string query: The query to pass to the reddit search function.  
        Returns:
            list[dict] highlights: list of highlight key-value pairs
        '''

        logging.info('grabbing goals from /r/soccer') 
        highlights = []

        for post in self.reddit.subreddit('soccer').search('{} flair:media'.format(query), limit=8):
            if self.is_goal_to_post(post.title):
                logging.info('adding post: {} | {}'.format(post.title, post.created_utc))
                highlights.append({'title' : post.title, 'link' : post.url, 'comments' : post.permalink})

        return highlights

    def search_highlights_by_player(self, player, club):
        '''
        Searches /r/soccer for video clip links containing a player's name. Posts are filtered
        with the flair "media" so that highlights are queried.
        Args:
            string player: Player name to search
            string club: Club name to include in the query alongside player name
        Returns:
            set playerHighlights: list of highlights in key-value form ( {title : link} )
        '''

        return self.search_subreddit(player + ' ' + club) #search the subreddit by full name of player
    
    def search_highlights_by_team(self, club):
        '''
        Searches /r/soccer for video clip links containing a team name. Posts are filtered
        with the flair "media" so that highlights are queried.
        Args:
            string club: Club name to include in the query alongside player name
        Returns:
            set playerHighlights: list of highlights in key-value form ( {title : link} )
        '''

        return self.search_subreddit(club)