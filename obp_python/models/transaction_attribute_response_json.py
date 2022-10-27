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


class TransactionAttributeResponseJson(object):
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
        'transaction_attribute_id': 'str',
        'name': 'str',
        'type': 'str',
        'value': 'str'
    }

    attribute_map = {
        'transaction_attribute_id': 'transaction_attribute_id',
        'name': 'name',
        'type': 'type',
        'value': 'value'
    }

    def __init__(self, transaction_attribute_id=None, name=None, type=None, value=None, _configuration=None):  # noqa: E501
        """TransactionAttributeResponseJson - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._transaction_attribute_id = None
        self._name = None
        self._type = None
        self._value = None
        self.discriminator = None

        self.transaction_attribute_id = transaction_attribute_id
        self.name = name
        self.type = type
        self.value = value

    @property
    def transaction_attribute_id(self):
        """Gets the transaction_attribute_id of this TransactionAttributeResponseJson.  # noqa: E501


        :return: The transaction_attribute_id of this TransactionAttributeResponseJson.  # noqa: E501
        :rtype: str
        """
        return self._transaction_attribute_id

    @transaction_attribute_id.setter
    def transaction_attribute_id(self, transaction_attribute_id):
        """Sets the transaction_attribute_id of this TransactionAttributeResponseJson.


        :param transaction_attribute_id: The transaction_attribute_id of this TransactionAttributeResponseJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and transaction_attribute_id is None:
            raise ValueError("Invalid value for `transaction_attribute_id`, must not be `None`")  # noqa: E501

        self._transaction_attribute_id = transaction_attribute_id

    @property
    def name(self):
        """Gets the name of this TransactionAttributeResponseJson.  # noqa: E501


        :return: The name of this TransactionAttributeResponseJson.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TransactionAttributeResponseJson.


        :param name: The name of this TransactionAttributeResponseJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this TransactionAttributeResponseJson.  # noqa: E501


        :return: The type of this TransactionAttributeResponseJson.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TransactionAttributeResponseJson.


        :param type: The type of this TransactionAttributeResponseJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def value(self):
        """Gets the value of this TransactionAttributeResponseJson.  # noqa: E501


        :return: The value of this TransactionAttributeResponseJson.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TransactionAttributeResponseJson.


        :param value: The value of this TransactionAttributeResponseJson.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if issubclass(TransactionAttributeResponseJson, dict):
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
        if not isinstance(other, TransactionAttributeResponseJson):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransactionAttributeResponseJson):
            return True

        return self.to_dict() != other.to_dict()