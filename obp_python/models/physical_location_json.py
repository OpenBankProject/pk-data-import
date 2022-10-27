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


class PhysicalLocationJSON(object):
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
        'physical_location': 'LocationPlainJSON'
    }

    attribute_map = {
        'physical_location': 'physical_location'
    }

    def __init__(self, physical_location=None, _configuration=None):  # noqa: E501
        """PhysicalLocationJSON - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._physical_location = None
        self.discriminator = None

        self.physical_location = physical_location

    @property
    def physical_location(self):
        """Gets the physical_location of this PhysicalLocationJSON.  # noqa: E501


        :return: The physical_location of this PhysicalLocationJSON.  # noqa: E501
        :rtype: LocationPlainJSON
        """
        return self._physical_location

    @physical_location.setter
    def physical_location(self, physical_location):
        """Sets the physical_location of this PhysicalLocationJSON.


        :param physical_location: The physical_location of this PhysicalLocationJSON.  # noqa: E501
        :type: LocationPlainJSON
        """
        if self._configuration.client_side_validation and physical_location is None:
            raise ValueError("Invalid value for `physical_location`, must not be `None`")  # noqa: E501

        self._physical_location = physical_location

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
        if issubclass(PhysicalLocationJSON, dict):
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
        if not isinstance(other, PhysicalLocationJSON):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PhysicalLocationJSON):
            return True

        return self.to_dict() != other.to_dict()
