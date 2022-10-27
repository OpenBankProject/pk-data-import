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


class PostConsentRequestJsonV500(object):
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
        'phone_number': 'str',
        'time_to_live': 'int',
        'email': 'str',
        'account_access': 'list[AccountAccessV500]',
        'everything': 'bool',
        'consumer_id': 'str',
        'valid_from': 'date',
        'entitlements': 'list[PostConsentEntitlementJsonV310]'
    }

    attribute_map = {
        'phone_number': 'phone_number',
        'time_to_live': 'time_to_live',
        'email': 'email',
        'account_access': 'account_access',
        'everything': 'everything',
        'consumer_id': 'consumer_id',
        'valid_from': 'valid_from',
        'entitlements': 'entitlements'
    }

    def __init__(self, phone_number=None, time_to_live=None, email=None, account_access=None, everything=None, consumer_id=None, valid_from=None, entitlements=None, _configuration=None):  # noqa: E501
        """PostConsentRequestJsonV500 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._phone_number = None
        self._time_to_live = None
        self._email = None
        self._account_access = None
        self._everything = None
        self._consumer_id = None
        self._valid_from = None
        self._entitlements = None
        self.discriminator = None

        if phone_number is not None:
            self.phone_number = phone_number
        if time_to_live is not None:
            self.time_to_live = time_to_live
        if email is not None:
            self.email = email
        self.account_access = account_access
        self.everything = everything
        if consumer_id is not None:
            self.consumer_id = consumer_id
        if valid_from is not None:
            self.valid_from = valid_from
        if entitlements is not None:
            self.entitlements = entitlements

    @property
    def phone_number(self):
        """Gets the phone_number of this PostConsentRequestJsonV500.  # noqa: E501


        :return: The phone_number of this PostConsentRequestJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this PostConsentRequestJsonV500.


        :param phone_number: The phone_number of this PostConsentRequestJsonV500.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

    @property
    def time_to_live(self):
        """Gets the time_to_live of this PostConsentRequestJsonV500.  # noqa: E501


        :return: The time_to_live of this PostConsentRequestJsonV500.  # noqa: E501
        :rtype: int
        """
        return self._time_to_live

    @time_to_live.setter
    def time_to_live(self, time_to_live):
        """Sets the time_to_live of this PostConsentRequestJsonV500.


        :param time_to_live: The time_to_live of this PostConsentRequestJsonV500.  # noqa: E501
        :type: int
        """

        self._time_to_live = time_to_live

    @property
    def email(self):
        """Gets the email of this PostConsentRequestJsonV500.  # noqa: E501


        :return: The email of this PostConsentRequestJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this PostConsentRequestJsonV500.


        :param email: The email of this PostConsentRequestJsonV500.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def account_access(self):
        """Gets the account_access of this PostConsentRequestJsonV500.  # noqa: E501


        :return: The account_access of this PostConsentRequestJsonV500.  # noqa: E501
        :rtype: list[AccountAccessV500]
        """
        return self._account_access

    @account_access.setter
    def account_access(self, account_access):
        """Sets the account_access of this PostConsentRequestJsonV500.


        :param account_access: The account_access of this PostConsentRequestJsonV500.  # noqa: E501
        :type: list[AccountAccessV500]
        """
        if self._configuration.client_side_validation and account_access is None:
            raise ValueError("Invalid value for `account_access`, must not be `None`")  # noqa: E501

        self._account_access = account_access

    @property
    def everything(self):
        """Gets the everything of this PostConsentRequestJsonV500.  # noqa: E501


        :return: The everything of this PostConsentRequestJsonV500.  # noqa: E501
        :rtype: bool
        """
        return self._everything

    @everything.setter
    def everything(self, everything):
        """Sets the everything of this PostConsentRequestJsonV500.


        :param everything: The everything of this PostConsentRequestJsonV500.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and everything is None:
            raise ValueError("Invalid value for `everything`, must not be `None`")  # noqa: E501

        self._everything = everything

    @property
    def consumer_id(self):
        """Gets the consumer_id of this PostConsentRequestJsonV500.  # noqa: E501


        :return: The consumer_id of this PostConsentRequestJsonV500.  # noqa: E501
        :rtype: str
        """
        return self._consumer_id

    @consumer_id.setter
    def consumer_id(self, consumer_id):
        """Sets the consumer_id of this PostConsentRequestJsonV500.


        :param consumer_id: The consumer_id of this PostConsentRequestJsonV500.  # noqa: E501
        :type: str
        """

        self._consumer_id = consumer_id

    @property
    def valid_from(self):
        """Gets the valid_from of this PostConsentRequestJsonV500.  # noqa: E501


        :return: The valid_from of this PostConsentRequestJsonV500.  # noqa: E501
        :rtype: date
        """
        return self._valid_from

    @valid_from.setter
    def valid_from(self, valid_from):
        """Sets the valid_from of this PostConsentRequestJsonV500.


        :param valid_from: The valid_from of this PostConsentRequestJsonV500.  # noqa: E501
        :type: date
        """

        self._valid_from = valid_from

    @property
    def entitlements(self):
        """Gets the entitlements of this PostConsentRequestJsonV500.  # noqa: E501


        :return: The entitlements of this PostConsentRequestJsonV500.  # noqa: E501
        :rtype: list[PostConsentEntitlementJsonV310]
        """
        return self._entitlements

    @entitlements.setter
    def entitlements(self, entitlements):
        """Sets the entitlements of this PostConsentRequestJsonV500.


        :param entitlements: The entitlements of this PostConsentRequestJsonV500.  # noqa: E501
        :type: list[PostConsentEntitlementJsonV310]
        """

        self._entitlements = entitlements

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
        if issubclass(PostConsentRequestJsonV500, dict):
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
        if not isinstance(other, PostConsentRequestJsonV500):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostConsentRequestJsonV500):
            return True

        return self.to_dict() != other.to_dict()
