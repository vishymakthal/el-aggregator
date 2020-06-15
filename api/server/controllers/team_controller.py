from flask import send_file
import connexion
import io
import requests
import six

from server.models.team import Team  # noqa: E501
from server.services import algolia_search

def get_team_by_id(team_id):  # noqa: E501
    """Find team by ID

    Returns a single team # noqa: E501

    :param teamId: ID of the team to return
    :type teamId: int

    :rtype: Team
    """
    return algolia_search.get_team(team_id)

def get_team_img_by_id(team_id):
    """Get team's image from Sofifa

    Returns a png

    :param team_id: ID of player to retrieve image for
    :type team_id: str
    """

    r = requests.get('https://cdn.sofifa.com/teams/{}/light_240.png'.format(team_id))
    if r.status_code != 200:
        return 'error grabbing image', 500
    
    return send_file(
        io.BytesIO(r.content),
        mimetype='image/png',
    )