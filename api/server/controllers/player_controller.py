import connexion
import six

from server.models.player import Player  # noqa: E501
from server.services import firebase 

def get_player_by_id(player_id):  # noqa: E501
    """Find player by ID

    Returns a single player # noqa: E501

    :param playerId: ID of player to return
    :type playerId: int

    :rtype: Player
    """

    return firebase.read('players', player_id) 
