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


class AccountWebhookPutJson(object):
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
        'account_webhook_id': 'str',
        'is_active': 'str'
    }

    attribute_map = {
        'account_webhook_id': 'account_webhook_id',
        'is_active': 'is_active'
    }

    def __init__(self, account_webhook_id=None, is_active=None, _configuration=None):  # noqa: E501
        """AccountWebhookPutJson - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_webhook_id = None
        self._is_active = None
        self.discriminator = None

        self.account_webhook_id = account_webhook_id
        self.is_active = is_active

    @property
    def account_webhook_id(self):
        """Gets the account_webhook_id of this AccountWebhookPutJson.  # noqa: E501


        :return: The account_webhook_id of this AccountWebhookPutJson.  # noqa: E501
        :rtype: str
        """
        return self._account_webhook_id

    @account_webhook_id.setter
    def account_webhook_id(self, account_webhook_id):
        """Sets the account_webhook_id of this AccountWebhookPutJson.


        :param account_webhook_id: The account_webhook_id of this AccountWebhookPutJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and account_webhook_id is None:
            raise ValueError("Invalid value for `account_webhook_id`, must not be `None`")  # noqa: E501

        self._account_webhook_id = account_webhook_id

    @property
    def is_active(self):
        """Gets the is_active of this AccountWebhookPutJson.  # noqa: E501


        :return: The is_active of this AccountWebhookPutJson.  # noqa: E501
        :rtype: str
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this AccountWebhookPutJson.


        :param is_active: The is_active of this AccountWebhookPutJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and is_active is None:
            raise ValueError("Invalid value for `is_active`, must not be `None`")  # noqa: E501

        self._is_active = is_active

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
        if issubclass(AccountWebhookPutJson, dict):
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
        if not isinstance(other, AccountWebhookPutJson):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountWebhookPutJson):
            return True

        return self.to_dict() != other.to_dict()
