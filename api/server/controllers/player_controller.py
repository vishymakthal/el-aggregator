from flask import send_file
import connexion
import io
import requests
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

def get_player_img_by_id(player_id):
    """Get player's image from sofifa

    Returns a png

    :param playerId: ID of player to retrieve image for
    :type playerId: str
    """

    r = requests.get('https://cdn.sofifa.com/players/{}/{}/20_240.png'.format(player_id[:3],player_id[3:]))
    if r.status_code != 200:
        return 'error grabbing image', 500
    
    return send_file(
        io.BytesIO(r.content),
        mimetype='image/png',
    )
