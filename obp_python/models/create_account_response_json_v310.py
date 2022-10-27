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


class CreateAccountResponseJsonV310(object):
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
        'account_attributes': 'list[AccountAttributeResponseJson]',
        'branch_id': 'str',
        'account_routings': 'list[AccountRoutingJsonV121]',
        'label': 'str',
        'balance': 'AmountOfMoneyJsonV121',
        'user_id': 'str',
        'product_code': 'str',
        'account_id': 'str'
    }

    attribute_map = {
        'account_attributes': 'account_attributes',
        'branch_id': 'branch_id',
        'account_routings': 'account_routings',
        'label': 'label',
        'balance': 'balance',
        'user_id': 'user_id',
        'product_code': 'product_code',
        'account_id': 'account_id'
    }

    def __init__(self, account_attributes=None, branch_id=None, account_routings=None, label=None, balance=None, user_id=None, product_code=None, account_id=None, _configuration=None):  # noqa: E501
        """CreateAccountResponseJsonV310 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_attributes = None
        self._branch_id = None
        self._account_routings = None
        self._label = None
        self._balance = None
        self._user_id = None
        self._product_code = None
        self._account_id = None
        self.discriminator = None

        self.account_attributes = account_attributes
        self.branch_id = branch_id
        self.account_routings = account_routings
        self.label = label
        self.balance = balance
        self.user_id = user_id
        self.product_code = product_code
        self.account_id = account_id

    @property
    def account_attributes(self):
        """Gets the account_attributes of this CreateAccountResponseJsonV310.  # noqa: E501


        :return: The account_attributes of this CreateAccountResponseJsonV310.  # noqa: E501
        :rtype: list[AccountAttributeResponseJson]
        """
        return self._account_attributes

    @account_attributes.setter
    def account_attributes(self, account_attributes):
        """Sets the account_attributes of this CreateAccountResponseJsonV310.


        :param account_attributes: The account_attributes of this CreateAccountResponseJsonV310.  # noqa: E501
        :type: list[AccountAttributeResponseJson]
        """
        if self._configuration.client_side_validation and account_attributes is None:
            raise ValueError("Invalid value for `account_attributes`, must not be `None`")  # noqa: E501

        self._account_attributes = account_attributes

    @property
    def branch_id(self):
        """Gets the branch_id of this CreateAccountResponseJsonV310.  # noqa: E501


        :return: The branch_id of this CreateAccountResponseJsonV310.  # noqa: E501
        :rtype: str
        """
        return self._branch_id

    @branch_id.setter
    def branch_id(self, branch_id):
        """Sets the branch_id of this CreateAccountResponseJsonV310.


        :param branch_id: The branch_id of this CreateAccountResponseJsonV310.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and branch_id is None:
            raise ValueError("Invalid value for `branch_id`, must not be `None`")  # noqa: E501

        self._branch_id = branch_id

    @property
    def account_routings(self):
        """Gets the account_routings of this CreateAccountResponseJsonV310.  # noqa: E501


        :return: The account_routings of this CreateAccountResponseJsonV310.  # noqa: E501
        :rtype: list[AccountRoutingJsonV121]
        """
        return self._account_routings

    @account_routings.setter
    def account_routings(self, account_routings):
        """Sets the account_routings of this CreateAccountResponseJsonV310.


        :param account_routings: The account_routings of this CreateAccountResponseJsonV310.  # noqa: E501
        :type: list[AccountRoutingJsonV121]
        """
        if self._configuration.client_side_validation and account_routings is None:
            raise ValueError("Invalid value for `account_routings`, must not be `None`")  # noqa: E501

        self._account_routings = account_routings

    @property
    def label(self):
        """Gets the label of this CreateAccountResponseJsonV310.  # noqa: E501


        :return: The label of this CreateAccountResponseJsonV310.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this CreateAccountResponseJsonV310.


        :param label: The label of this CreateAccountResponseJsonV310.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def balance(self):
        """Gets the balance of this CreateAccountResponseJsonV310.  # noqa: E501


        :return: The balance of this CreateAccountResponseJsonV310.  # noqa: E501
        :rtype: AmountOfMoneyJsonV121
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this CreateAccountResponseJsonV310.


        :param balance: The balance of this CreateAccountResponseJsonV310.  # noqa: E501
        :type: AmountOfMoneyJsonV121
        """
        if self._configuration.client_side_validation and balance is None:
            raise ValueError("Invalid value for `balance`, must not be `None`")  # noqa: E501

        self._balance = balance

    @property
    def user_id(self):
        """Gets the user_id of this CreateAccountResponseJsonV310.  # noqa: E501


        :return: The user_id of this CreateAccountResponseJsonV310.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this CreateAccountResponseJsonV310.


        :param user_id: The user_id of this CreateAccountResponseJsonV310.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def product_code(self):
        """Gets the product_code of this CreateAccountResponseJsonV310.  # noqa: E501


        :return: The product_code of this CreateAccountResponseJsonV310.  # noqa: E501
        :rtype: str
        """
        return self._product_code

    @product_code.setter
    def product_code(self, product_code):
        """Sets the product_code of this CreateAccountResponseJsonV310.


        :param product_code: The product_code of this CreateAccountResponseJsonV310.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and product_code is None:
            raise ValueError("Invalid value for `product_code`, must not be `None`")  # noqa: E501

        self._product_code = product_code

    @property
    def account_id(self):
        """Gets the account_id of this CreateAccountResponseJsonV310.  # noqa: E501


        :return: The account_id of this CreateAccountResponseJsonV310.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this CreateAccountResponseJsonV310.


        :param account_id: The account_id of this CreateAccountResponseJsonV310.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

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
        if issubclass(CreateAccountResponseJsonV310, dict):
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
        if not isinstance(other, CreateAccountResponseJsonV310):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateAccountResponseJsonV310):
            return True

        return self.to_dict() != other.to_dict()
