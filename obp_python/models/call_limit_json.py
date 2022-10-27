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


class CallLimitJson(object):
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
        'current_state': 'RedisCallLimitJson',
        'per_month_call_limit': 'str',
        'per_week_call_limit': 'str',
        'per_hour_call_limit': 'str',
        'per_second_call_limit': 'str',
        'per_minute_call_limit': 'str',
        'per_day_call_limit': 'str'
    }

    attribute_map = {
        'current_state': 'current_state',
        'per_month_call_limit': 'per_month_call_limit',
        'per_week_call_limit': 'per_week_call_limit',
        'per_hour_call_limit': 'per_hour_call_limit',
        'per_second_call_limit': 'per_second_call_limit',
        'per_minute_call_limit': 'per_minute_call_limit',
        'per_day_call_limit': 'per_day_call_limit'
    }

    def __init__(self, current_state=None, per_month_call_limit=None, per_week_call_limit=None, per_hour_call_limit=None, per_second_call_limit=None, per_minute_call_limit=None, per_day_call_limit=None, _configuration=None):  # noqa: E501
        """CallLimitJson - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._current_state = None
        self._per_month_call_limit = None
        self._per_week_call_limit = None
        self._per_hour_call_limit = None
        self._per_second_call_limit = None
        self._per_minute_call_limit = None
        self._per_day_call_limit = None
        self.discriminator = None

        if current_state is not None:
            self.current_state = current_state
        self.per_month_call_limit = per_month_call_limit
        self.per_week_call_limit = per_week_call_limit
        self.per_hour_call_limit = per_hour_call_limit
        self.per_second_call_limit = per_second_call_limit
        self.per_minute_call_limit = per_minute_call_limit
        self.per_day_call_limit = per_day_call_limit

    @property
    def current_state(self):
        """Gets the current_state of this CallLimitJson.  # noqa: E501


        :return: The current_state of this CallLimitJson.  # noqa: E501
        :rtype: RedisCallLimitJson
        """
        return self._current_state

    @current_state.setter
    def current_state(self, current_state):
        """Sets the current_state of this CallLimitJson.


        :param current_state: The current_state of this CallLimitJson.  # noqa: E501
        :type: RedisCallLimitJson
        """

        self._current_state = current_state

    @property
    def per_month_call_limit(self):
        """Gets the per_month_call_limit of this CallLimitJson.  # noqa: E501


        :return: The per_month_call_limit of this CallLimitJson.  # noqa: E501
        :rtype: str
        """
        return self._per_month_call_limit

    @per_month_call_limit.setter
    def per_month_call_limit(self, per_month_call_limit):
        """Sets the per_month_call_limit of this CallLimitJson.


        :param per_month_call_limit: The per_month_call_limit of this CallLimitJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and per_month_call_limit is None:
            raise ValueError("Invalid value for `per_month_call_limit`, must not be `None`")  # noqa: E501

        self._per_month_call_limit = per_month_call_limit

    @property
    def per_week_call_limit(self):
        """Gets the per_week_call_limit of this CallLimitJson.  # noqa: E501


        :return: The per_week_call_limit of this CallLimitJson.  # noqa: E501
        :rtype: str
        """
        return self._per_week_call_limit

    @per_week_call_limit.setter
    def per_week_call_limit(self, per_week_call_limit):
        """Sets the per_week_call_limit of this CallLimitJson.


        :param per_week_call_limit: The per_week_call_limit of this CallLimitJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and per_week_call_limit is None:
            raise ValueError("Invalid value for `per_week_call_limit`, must not be `None`")  # noqa: E501

        self._per_week_call_limit = per_week_call_limit

    @property
    def per_hour_call_limit(self):
        """Gets the per_hour_call_limit of this CallLimitJson.  # noqa: E501


        :return: The per_hour_call_limit of this CallLimitJson.  # noqa: E501
        :rtype: str
        """
        return self._per_hour_call_limit

    @per_hour_call_limit.setter
    def per_hour_call_limit(self, per_hour_call_limit):
        """Sets the per_hour_call_limit of this CallLimitJson.


        :param per_hour_call_limit: The per_hour_call_limit of this CallLimitJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and per_hour_call_limit is None:
            raise ValueError("Invalid value for `per_hour_call_limit`, must not be `None`")  # noqa: E501

        self._per_hour_call_limit = per_hour_call_limit

    @property
    def per_second_call_limit(self):
        """Gets the per_second_call_limit of this CallLimitJson.  # noqa: E501


        :return: The per_second_call_limit of this CallLimitJson.  # noqa: E501
        :rtype: str
        """
        return self._per_second_call_limit

    @per_second_call_limit.setter
    def per_second_call_limit(self, per_second_call_limit):
        """Sets the per_second_call_limit of this CallLimitJson.


        :param per_second_call_limit: The per_second_call_limit of this CallLimitJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and per_second_call_limit is None:
            raise ValueError("Invalid value for `per_second_call_limit`, must not be `None`")  # noqa: E501

        self._per_second_call_limit = per_second_call_limit

    @property
    def per_minute_call_limit(self):
        """Gets the per_minute_call_limit of this CallLimitJson.  # noqa: E501


        :return: The per_minute_call_limit of this CallLimitJson.  # noqa: E501
        :rtype: str
        """
        return self._per_minute_call_limit

    @per_minute_call_limit.setter
    def per_minute_call_limit(self, per_minute_call_limit):
        """Sets the per_minute_call_limit of this CallLimitJson.


        :param per_minute_call_limit: The per_minute_call_limit of this CallLimitJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and per_minute_call_limit is None:
            raise ValueError("Invalid value for `per_minute_call_limit`, must not be `None`")  # noqa: E501

        self._per_minute_call_limit = per_minute_call_limit

    @property
    def per_day_call_limit(self):
        """Gets the per_day_call_limit of this CallLimitJson.  # noqa: E501


        :return: The per_day_call_limit of this CallLimitJson.  # noqa: E501
        :rtype: str
        """
        return self._per_day_call_limit

    @per_day_call_limit.setter
    def per_day_call_limit(self, per_day_call_limit):
        """Sets the per_day_call_limit of this CallLimitJson.


        :param per_day_call_limit: The per_day_call_limit of this CallLimitJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and per_day_call_limit is None:
            raise ValueError("Invalid value for `per_day_call_limit`, must not be `None`")  # noqa: E501

        self._per_day_call_limit = per_day_call_limit

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
        if issubclass(CallLimitJson, dict):
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
        if not isinstance(other, CallLimitJson):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CallLimitJson):
            return True

        return self.to_dict() != other.to_dict()
