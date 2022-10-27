# coding: utf-8

"""
    Open Bank Project API

    An Open Source API for Banks. (c) TESOBE GmbH. 2011 - 2022. Licensed under the AGPL and commercial licences.  # noqa: E501

    OpenAPI spec version: v5.0.0
    Contact: contact@tesobe.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from obp_python.configuration import Configuration


class SandboxBranchImport(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'location': 'SandboxLocationImport',
        'drive_up': 'SandboxDriveUpImport',
        'bank_id': 'str',
        'id': 'str',
        'meta': 'SandboxMetaImport',
        'lobby': 'SandboxLobbyImport',
        'address': 'SandboxAddressImport'
    }

    attribute_map = {
        'name': 'name',
        'location': 'location',
        'drive_up': 'driveUp',
        'bank_id': 'bank_id',
        'id': 'id',
        'meta': 'meta',
        'lobby': 'lobby',
        'address': 'address'
    }

    def __init__(self, name=None, location=None, drive_up=None, bank_id=None, id=None, meta=None, lobby=None, address=None, _configuration=None):  # noqa: E501
        """SandboxBranchImport - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._name = None
        self._location = None
        self._drive_up = None
        self._bank_id = None
        self._id = None
        self._meta = None
        self._lobby = None
        self._address = None
        self.discriminator = None

        self.name = name
        self.location = location
        if drive_up is not None:
            self.drive_up = drive_up
        self.bank_id = bank_id
        self.id = id
        self.meta = meta
        if lobby is not None:
            self.lobby = lobby
        self.address = address

    @property
    def name(self):
        """Gets the name of this SandboxBranchImport.  # noqa: E501


        :return: The name of this SandboxBranchImport.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SandboxBranchImport.


        :param name: The name of this SandboxBranchImport.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def location(self):
        """Gets the location of this SandboxBranchImport.  # noqa: E501


        :return: The location of this SandboxBranchImport.  # noqa: E501
        :rtype: SandboxLocationImport
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this SandboxBranchImport.


        :param location: The location of this SandboxBranchImport.  # noqa: E501
        :type: SandboxLocationImport
        """
        if self._configuration.client_side_validation and location is None:
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501

        self._location = location

    @property
    def drive_up(self):
        """Gets the drive_up of this SandboxBranchImport.  # noqa: E501


        :return: The drive_up of this SandboxBranchImport.  # noqa: E501
        :rtype: SandboxDriveUpImport
        """
        return self._drive_up

    @drive_up.setter
    def drive_up(self, drive_up):
        """Sets the drive_up of this SandboxBranchImport.


        :param drive_up: The drive_up of this SandboxBranchImport.  # noqa: E501
        :type: SandboxDriveUpImport
        """

        self._drive_up = drive_up

    @property
    def bank_id(self):
        """Gets the bank_id of this SandboxBranchImport.  # noqa: E501


        :return: The bank_id of this SandboxBranchImport.  # noqa: E501
        :rtype: str
        """
        return self._bank_id

    @bank_id.setter
    def bank_id(self, bank_id):
        """Sets the bank_id of this SandboxBranchImport.


        :param bank_id: The bank_id of this SandboxBranchImport.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and bank_id is None:
            raise ValueError("Invalid value for `bank_id`, must not be `None`")  # noqa: E501

        self._bank_id = bank_id

    @property
    def id(self):
        """Gets the id of this SandboxBranchImport.  # noqa: E501


        :return: The id of this SandboxBranchImport.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SandboxBranchImport.


        :param id: The id of this SandboxBranchImport.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def meta(self):
        """Gets the meta of this SandboxBranchImport.  # noqa: E501


        :return: The meta of this SandboxBranchImport.  # noqa: E501
        :rtype: SandboxMetaImport
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this SandboxBranchImport.


        :param meta: The meta of this SandboxBranchImport.  # noqa: E501
        :type: SandboxMetaImport
        """
        if self._configuration.client_side_validation and meta is None:
            raise ValueError("Invalid value for `meta`, must not be `None`")  # noqa: E501

        self._meta = meta

    @property
    def lobby(self):
        """Gets the lobby of this SandboxBranchImport.  # noqa: E501


        :return: The lobby of this SandboxBranchImport.  # noqa: E501
        :rtype: SandboxLobbyImport
        """
        return self._lobby

    @lobby.setter
    def lobby(self, lobby):
        """Sets the lobby of this SandboxBranchImport.


        :param lobby: The lobby of this SandboxBranchImport.  # noqa: E501
        :type: SandboxLobbyImport
        """

        self._lobby = lobby

    @property
    def address(self):
        """Gets the address of this SandboxBranchImport.  # noqa: E501


        :return: The address of this SandboxBranchImport.  # noqa: E501
        :rtype: SandboxAddressImport
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this SandboxBranchImport.


        :param address: The address of this SandboxBranchImport.  # noqa: E501
        :type: SandboxAddressImport
        """
        if self._configuration.client_side_validation and address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SandboxBranchImport, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SandboxBranchImport):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SandboxBranchImport):
            return True

        return self.to_dict() != other.to_dict()