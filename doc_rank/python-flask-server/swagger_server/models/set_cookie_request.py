# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SetCookieRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, cookie: str=None):  # noqa: E501
        """SetCookieRequest - a model defined in Swagger

        :param cookie: The cookie of this SetCookieRequest.  # noqa: E501
        :type cookie: str
        """
        self.swagger_types = {
            'cookie': str
        }

        self.attribute_map = {
            'cookie': 'cookie'
        }

        self._cookie = cookie

    @classmethod
    def from_dict(cls, dikt) -> 'SetCookieRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SetCookieRequest of this SetCookieRequest.  # noqa: E501
        :rtype: SetCookieRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cookie(self) -> str:
        """Gets the cookie of this SetCookieRequest.


        :return: The cookie of this SetCookieRequest.
        :rtype: str
        """
        return self._cookie

    @cookie.setter
    def cookie(self, cookie: str):
        """Sets the cookie of this SetCookieRequest.


        :param cookie: The cookie of this SetCookieRequest.
        :type cookie: str
        """

        self._cookie = cookie
