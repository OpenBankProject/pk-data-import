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


class EmptyClassJson(object):
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
        'json_string': 'str'
    }

    attribute_map = {
        'json_string': 'jsonString'
    }

    def __init__(self, json_string=None, _configuration=None):  # noqa: E501
        """EmptyClassJson - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._json_string = None
        self.discriminator = None

        self.json_string = json_string

    @property
    def json_string(self):
        """Gets the json_string of this EmptyClassJson.  # noqa: E501


        :return: The json_string of this EmptyClassJson.  # noqa: E501
        :rtype: str
        """
        return self._json_string

    @json_string.setter
    def json_string(self, json_string):
        """Sets the json_string of this EmptyClassJson.


        :param json_string: The json_string of this EmptyClassJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and json_string is None:
            raise ValueError("Invalid value for `json_string`, must not be `None`")  # noqa: E501

        self._json_string = json_string

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
        if issubclass(EmptyClassJson, dict):
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
        if not isinstance(other, EmptyClassJson):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EmptyClassJson):
            return True

        return self.to_dict() != other.to_dict()
