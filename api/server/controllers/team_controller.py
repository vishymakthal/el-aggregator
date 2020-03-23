import connexion
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
