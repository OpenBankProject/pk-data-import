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


class SandboxAccountImport(object):
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
        'generate_auditors_view': 'bool',
        'number': 'str',
        'iban': 'str',
        'label': 'str',
        'owners': 'list[str]',
        'balance': 'SandboxBalanceImport',
        'bank': 'str',
        'id': 'str',
        'type': 'str',
        'generate_accountants_view': 'bool',
        'generate_public_view': 'bool'
    }

    attribute_map = {
        'generate_auditors_view': 'generate_auditors_view',
        'number': 'number',
        'iban': 'IBAN',
        'label': 'label',
        'owners': 'owners',
        'balance': 'balance',
        'bank': 'bank',
        'id': 'id',
        'type': 'type',
        'generate_accountants_view': 'generate_accountants_view',
        'generate_public_view': 'generate_public_view'
    }

    def __init__(self, generate_auditors_view=None, number=None, iban=None, label=None, owners=None, balance=None, bank=None, id=None, type=None, generate_accountants_view=None, generate_public_view=None, _configuration=None):  # noqa: E501
        """SandboxAccountImport - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._generate_auditors_view = None
        self._number = None
        self._iban = None
        self._label = None
        self._owners = None
        self._balance = None
        self._bank = None
        self._id = None
        self._type = None
        self._generate_accountants_view = None
        self._generate_public_view = None
        self.discriminator = None

        self.generate_auditors_view = generate_auditors_view
        self.number = number
        self.iban = iban
        self.label = label
        self.owners = owners
        self.balance = balance
        self.bank = bank
        self.id = id
        self.type = type
        self.generate_accountants_view = generate_accountants_view
        self.generate_public_view = generate_public_view

    @property
    def generate_auditors_view(self):
        """Gets the generate_auditors_view of this SandboxAccountImport.  # noqa: E501


        :return: The generate_auditors_view of this SandboxAccountImport.  # noqa: E501
        :rtype: bool
        """
        return self._generate_auditors_view

    @generate_auditors_view.setter
    def generate_auditors_view(self, generate_auditors_view):
        """Sets the generate_auditors_view of this SandboxAccountImport.


        :param generate_auditors_view: The generate_auditors_view of this SandboxAccountImport.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and generate_auditors_view is None:
            raise ValueError("Invalid value for `generate_auditors_view`, must not be `None`")  # noqa: E501

        self._generate_auditors_view = generate_auditors_view

    @property
    def number(self):
        """Gets the number of this SandboxAccountImport.  # noqa: E501


        :return: The number of this SandboxAccountImport.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this SandboxAccountImport.


        :param number: The number of this SandboxAccountImport.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and number is None:
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501

        self._number = number

    @property
    def iban(self):
        """Gets the iban of this SandboxAccountImport.  # noqa: E501


        :return: The iban of this SandboxAccountImport.  # noqa: E501
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this SandboxAccountImport.


        :param iban: The iban of this SandboxAccountImport.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and iban is None:
            raise ValueError("Invalid value for `iban`, must not be `None`")  # noqa: E501

        self._iban = iban

    @property
    def label(self):
        """Gets the label of this SandboxAccountImport.  # noqa: E501


        :return: The label of this SandboxAccountImport.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this SandboxAccountImport.


        :param label: The label of this SandboxAccountImport.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def owners(self):
        """Gets the owners of this SandboxAccountImport.  # noqa: E501


        :return: The owners of this SandboxAccountImport.  # noqa: E501
        :rtype: list[str]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """Sets the owners of this SandboxAccountImport.


        :param owners: The owners of this SandboxAccountImport.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and owners is None:
            raise ValueError("Invalid value for `owners`, must not be `None`")  # noqa: E501

        self._owners = owners

    @property
    def balance(self):
        """Gets the balance of this SandboxAccountImport.  # noqa: E501


        :return: The balance of this SandboxAccountImport.  # noqa: E501
        :rtype: SandboxBalanceImport
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this SandboxAccountImport.


        :param balance: The balance of this SandboxAccountImport.  # noqa: E501
        :type: SandboxBalanceImport
        """
        if self._configuration.client_side_validation and balance is None:
            raise ValueError("Invalid value for `balance`, must not be `None`")  # noqa: E501

        self._balance = balance

    @property
    def bank(self):
        """Gets the bank of this SandboxAccountImport.  # noqa: E501


        :return: The bank of this SandboxAccountImport.  # noqa: E501
        :rtype: str
        """
        return self._bank

    @bank.setter
    def bank(self, bank):
        """Sets the bank of this SandboxAccountImport.


        :param bank: The bank of this SandboxAccountImport.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and bank is None:
            raise ValueError("Invalid value for `bank`, must not be `None`")  # noqa: E501

        self._bank = bank

    @property
    def id(self):
        """Gets the id of this SandboxAccountImport.  # noqa: E501


        :return: The id of this SandboxAccountImport.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SandboxAccountImport.


        :param id: The id of this SandboxAccountImport.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this SandboxAccountImport.  # noqa: E501


        :return: The type of this SandboxAccountImport.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SandboxAccountImport.


        :param type: The type of this SandboxAccountImport.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def generate_accountants_view(self):
        """Gets the generate_accountants_view of this SandboxAccountImport.  # noqa: E501


        :return: The generate_accountants_view of this SandboxAccountImport.  # noqa: E501
        :rtype: bool
        """
        return self._generate_accountants_view

    @generate_accountants_view.setter
    def generate_accountants_view(self, generate_accountants_view):
        """Sets the generate_accountants_view of this SandboxAccountImport.


        :param generate_accountants_view: The generate_accountants_view of this SandboxAccountImport.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and generate_accountants_view is None:
            raise ValueError("Invalid value for `generate_accountants_view`, must not be `None`")  # noqa: E501

        self._generate_accountants_view = generate_accountants_view

    @property
    def generate_public_view(self):
        """Gets the generate_public_view of this SandboxAccountImport.  # noqa: E501


        :return: The generate_public_view of this SandboxAccountImport.  # noqa: E501
        :rtype: bool
        """
        return self._generate_public_view

    @generate_public_view.setter
    def generate_public_view(self, generate_public_view):
        """Sets the generate_public_view of this SandboxAccountImport.


        :param generate_public_view: The generate_public_view of this SandboxAccountImport.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and generate_public_view is None:
            raise ValueError("Invalid value for `generate_public_view`, must not be `None`")  # noqa: E501

        self._generate_public_view = generate_public_view

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
        if issubclass(SandboxAccountImport, dict):
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
        if not isinstance(other, SandboxAccountImport):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SandboxAccountImport):
            return True

        return self.to_dict() != other.to_dict()
