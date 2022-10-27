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


class MeetingKeysJson(object):
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
        'session_id': 'str',
        'staff_token': 'str',
        'customer_token': 'str'
    }

    attribute_map = {
        'session_id': 'session_id',
        'staff_token': 'staff_token',
        'customer_token': 'customer_token'
    }

    def __init__(self, session_id=None, staff_token=None, customer_token=None, _configuration=None):  # noqa: E501
        """MeetingKeysJson - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._session_id = None
        self._staff_token = None
        self._customer_token = None
        self.discriminator = None

        self.session_id = session_id
        self.staff_token = staff_token
        self.customer_token = customer_token

    @property
    def session_id(self):
        """Gets the session_id of this MeetingKeysJson.  # noqa: E501


        :return: The session_id of this MeetingKeysJson.  # noqa: E501
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this MeetingKeysJson.


        :param session_id: The session_id of this MeetingKeysJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and session_id is None:
            raise ValueError("Invalid value for `session_id`, must not be `None`")  # noqa: E501

        self._session_id = session_id

    @property
    def staff_token(self):
        """Gets the staff_token of this MeetingKeysJson.  # noqa: E501


        :return: The staff_token of this MeetingKeysJson.  # noqa: E501
        :rtype: str
        """
        return self._staff_token

    @staff_token.setter
    def staff_token(self, staff_token):
        """Sets the staff_token of this MeetingKeysJson.


        :param staff_token: The staff_token of this MeetingKeysJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and staff_token is None:
            raise ValueError("Invalid value for `staff_token`, must not be `None`")  # noqa: E501

        self._staff_token = staff_token

    @property
    def customer_token(self):
        """Gets the customer_token of this MeetingKeysJson.  # noqa: E501


        :return: The customer_token of this MeetingKeysJson.  # noqa: E501
        :rtype: str
        """
        return self._customer_token

    @customer_token.setter
    def customer_token(self, customer_token):
        """Sets the customer_token of this MeetingKeysJson.


        :param customer_token: The customer_token of this MeetingKeysJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and customer_token is None:
            raise ValueError("Invalid value for `customer_token`, must not be `None`")  # noqa: E501

        self._customer_token = customer_token

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
        if issubclass(MeetingKeysJson, dict):
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
        if not isinstance(other, MeetingKeysJson):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MeetingKeysJson):
            return True

        return self.to_dict() != other.to_dict()
