from flask import send_file
import connexion
import io
import requests
import six


from server.models.player import Player  # noqa: E501
from server.services import firebase 

ATTACK = {'ST','RS','LS','CF','LW','RW'}
DEFENSE = {'CB','LWB','LB','RB','RWB'}
GOALKEEPER = {'GK'}

def get_player_by_id(player_id):  # noqa: E501
    """Find player by ID

    Returns a single player # noqa: E501

    :param playerId: ID of player to return
    :type playerId: int

    :rtype: Player
    """

    return firebase.read('players', player_id) 

def get_player_img_by_id(player_id):
    """Get player's image from Sofifa

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

def get_players_by_team_name(team_name):
    """Get players from a specific team within the database

    Returns List[Player]

    :param team_name: Name of team to get players for 
    :type team_name: str
    """

    return firebase.query_by_club('players', team_name)

def get_and_split_players_by_team_name(team_name):
    """Get players from a specific team and split them into smaller lists
         based on position.

    Returns List[List[Player]]

    :param team_name: Name of team to get players for 
    :type team_name: str
    """

    squad = get_players_by_team_name(team_name)
    
    if squad == 404:
        return 404
    
    defense = []; midfield = []; attack = []; goalkeepers = []
    for player in squad.values():
        if player['player_positions'][:2] in ATTACK:
            attack.append(player)
        elif player['player_positions'][:2] in DEFENSE:
            defense.append(player)
        elif player['player_positions'][:2] in GOALKEEPER:
            goalkeepers.append(player)
        else:
            midfield.append(player) # "Just go run around a bit" - Harry Redknapp
    
    return {'attack' : attack, 'midfield' : midfield, 'defense' : defense, 'gk' : goalkeepers}