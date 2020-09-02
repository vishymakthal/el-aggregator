from flask import send_file
import connexion
import io
import requests
import six


from server.models.player import Player  # noqa: E501

from server.cache import C

from server.services import firebase
from server.services import sofifa
from server.services import wiki
from server.services import reddit
from server.services import youtube
from server.services import transfermarkt 

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
    
    if C.has('obj_' + player_id):
        return C.read_record(player_id) 
    
    res = firebase.read('players', player_id)
    if res != {}:
        res['bio'] = wiki.get_bio(res['long_name'], res['short_name'])
        res['reddit'] = {'goals' : reddit.search_highlights_by_player(res['short_name'].split(' ')[-1], res['club'])}
        res['youtube'] = {'highlights' : youtube.search_youtube_by_player_name(res['short_name'], res['club'])}
        t = transfermarkt.new_player_profile(res['long_name'])
        res['transfermarkt'] = {'similar_players': [], 'url': t.get_url()}
    
    C.write_record(player_id, res)
    
    return res

def get_player_img_by_id(player_id):
    """Get player's image from Sofifa

    Returns a png

    :param playerId: ID of player to retrieve image for
    :type playerId: str
    """
    
    if C.has('img_' + player_id):
        print('reading from img cache')
        return send_file(open('img_' + player_id + '.eac', 'rb'), mimetype='image/png')

    r = requests.get('https://cdn.sofifa.com/players/{}/{}/20_240.png'.format(player_id[:3],player_id[3:]))
    if r.status_code != 200:
        return 'error grabbing image', 500

    print('caching img')
    C.write_img(player_id, r.content)

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

def get_full_squad(team_ext):
    """Get players from a specific team and split them into smaller lists
         based on position.

    Returns List[Player]

    :param team_name: Name of team to get players for 
    :type team_name: str
    """

    return sofifa.get_full_squad_list(team_ext)

def get_and_split_players_by_team_id(team_id):
    """Get players from a specific team and split them into smaller lists
         based on position.

    Returns List[List[Player]]

    :param team_name: Name of team to get players for 
    :type team_name: str
    """

    squad = get_full_squad(team_id)
    
    if squad == 404:
        return 404
    defense = []; midfield = []; attack = []; goalkeepers = []
    
    for player in squad:
        if player['position'] in ATTACK:
            attack.append(player)
        elif player['position'] in DEFENSE:
            defense.append(player)
        elif player['position'] in GOALKEEPER:
            goalkeepers.append(player)
        else:
            # "Just go run around a bit" - Harry Redknapp
            midfield.append(player)     
    return {'attack' : attack, 'midfield' : midfield, 'defense' : defense, 'gk' : goalkeepers}

def get_player_bio_by_name(player_name):
    """Get a player's Wikipedia bio.

    Returns String 

    :param player_name: player_name 
    :type player_name: str
    """

    return wiki.get_bio(player_name)

def search_players_by_name(query):
    """Get a player's Wikipedia bio.

    Returns List[Player] 

    :param query: query 
    :type query: str
    """
    return firebase.query_by_name('players', query)

def get_highlights_from_reddit(query):
    """Get /r/soccer highlights for a player.

    Returns List[Dict] 

    :param query: query in the format Name|Team 
    :type query: str
    """
    player, team = query.split('|')
    return reddit.search_highlights_by_player(player, team)