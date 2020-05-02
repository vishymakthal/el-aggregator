# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from server.models.base_model_ import Model
from server import util


class Team(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, league: str=None, name: str=None):  # noqa: E501
        """Team - a model defined in Swagger

        :param id: The id of this Team.  # noqa: E501
        :type id: int
        :param league: The league of this Team.  # noqa: E501
        :type league: str
        :param name: The name of this Team.  # noqa: E501
        :type name: str
        """
        self.swagger_types = {
            'id': int,
            'league': str,
            'name': str
        }

        self.attribute_map = {
            'id': 'id',
            'league': 'league',
            'name': 'name'
        }

        self._id = id
        self._league = league
        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'Team':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Team of this Team.  # noqa: E501
        :rtype: Team
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Team.


        :return: The id of this Team.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Team.


        :param id: The id of this Team.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def league(self) -> str:
        """Gets the league of this Team.


        :return: The league of this Team.
        :rtype: str
        """
        return self._league

    @league.setter
    def league(self, league: str):
        """Sets the league of this Team.


        :param league: The league of this Team.
        :type league: str
        """

        self._league = league

    @property
    def name(self) -> str:
        """Gets the name of this Team.


        :return: The name of this Team.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Team.


        :param name: The name of this Team.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name