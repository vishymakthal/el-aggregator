from algoliasearch.search_client import SearchClient
from algoliasearch.exceptions import RequestException

from server.config import cfg

class Algolia:

    def __init__(self):
        self.client = SearchClient.create(cfg.ALGOLIA_ID, cfg.ALGOLIA_KEY)
        self.team_index = self.client.init_index(cfg.ALGOLIA_TEAM_INDEX)
        self.player_index = self.client.init_index(cfg.ALGOLIA_PLAYER_INDEX)
    
    def get_object_by_key(self, index, key):
        return index.get_object(key)

    def get_player(self, key):
        try:
            return self.get_object_by_key(self.player_index, key)
        except RequestException:
            return ''
    
    def get_team(self, key):
        try:            
            return self.get_object_by_key(self.team_index, key)
        except RequestException:
            return ''
