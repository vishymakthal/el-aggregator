import connexion
import six

from server.models.player import Player  # noqa: E501
from server.services import algolia_search

def get_player_by_id(player_id):  # noqa: E501
    """Find player by ID

    Returns a single player # noqa: E501

    :param playerId: ID of player to return
    :type playerId: int

    :rtype: Player
    """

    return algolia_search.get_player(player_id)
