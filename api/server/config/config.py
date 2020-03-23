import os

class Config:
    def __init__(self):
        self.ALGOLIA_ID = os.getenv('ALGOLIA_ID')
        self.ALGOLIA_KEY = os.getenv('ALGOLIA_KEY')
        self.ALGOLIA_TEAM_INDEX = os.getenv('ALGOLIA_TEAM_INDEX')
        self.ALGOLIA_PLAYER_INDEX = os.getenv('ALGOLIA_PLAYER_INDEX')
