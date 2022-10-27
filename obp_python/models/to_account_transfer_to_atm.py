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


class ToAccountTransferToAtm(object):
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
        'legal_name': 'str',
        'date_of_birth': 'str',
        'mobile_phone_number': 'str',
        'kyc_document': 'ToAccountTransferToAtmKycDocument'
    }

    attribute_map = {
        'legal_name': 'legal_name',
        'date_of_birth': 'date_of_birth',
        'mobile_phone_number': 'mobile_phone_number',
        'kyc_document': 'kyc_document'
    }

    def __init__(self, legal_name=None, date_of_birth=None, mobile_phone_number=None, kyc_document=None, _configuration=None):  # noqa: E501
        """ToAccountTransferToAtm - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._legal_name = None
        self._date_of_birth = None
        self._mobile_phone_number = None
        self._kyc_document = None
        self.discriminator = None

        self.legal_name = legal_name
        self.date_of_birth = date_of_birth
        self.mobile_phone_number = mobile_phone_number
        self.kyc_document = kyc_document

    @property
    def legal_name(self):
        """Gets the legal_name of this ToAccountTransferToAtm.  # noqa: E501


        :return: The legal_name of this ToAccountTransferToAtm.  # noqa: E501
        :rtype: str
        """
        return self._legal_name

    @legal_name.setter
    def legal_name(self, legal_name):
        """Sets the legal_name of this ToAccountTransferToAtm.


        :param legal_name: The legal_name of this ToAccountTransferToAtm.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and legal_name is None:
            raise ValueError("Invalid value for `legal_name`, must not be `None`")  # noqa: E501

        self._legal_name = legal_name

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this ToAccountTransferToAtm.  # noqa: E501


        :return: The date_of_birth of this ToAccountTransferToAtm.  # noqa: E501
        :rtype: str
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this ToAccountTransferToAtm.


        :param date_of_birth: The date_of_birth of this ToAccountTransferToAtm.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and date_of_birth is None:
            raise ValueError("Invalid value for `date_of_birth`, must not be `None`")  # noqa: E501

        self._date_of_birth = date_of_birth

    @property
    def mobile_phone_number(self):
        """Gets the mobile_phone_number of this ToAccountTransferToAtm.  # noqa: E501


        :return: The mobile_phone_number of this ToAccountTransferToAtm.  # noqa: E501
        :rtype: str
        """
        return self._mobile_phone_number

    @mobile_phone_number.setter
    def mobile_phone_number(self, mobile_phone_number):
        """Sets the mobile_phone_number of this ToAccountTransferToAtm.


        :param mobile_phone_number: The mobile_phone_number of this ToAccountTransferToAtm.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and mobile_phone_number is None:
            raise ValueError("Invalid value for `mobile_phone_number`, must not be `None`")  # noqa: E501

        self._mobile_phone_number = mobile_phone_number

    @property
    def kyc_document(self):
        """Gets the kyc_document of this ToAccountTransferToAtm.  # noqa: E501


        :return: The kyc_document of this ToAccountTransferToAtm.  # noqa: E501
        :rtype: ToAccountTransferToAtmKycDocument
        """
        return self._kyc_document

    @kyc_document.setter
    def kyc_document(self, kyc_document):
        """Sets the kyc_document of this ToAccountTransferToAtm.


        :param kyc_document: The kyc_document of this ToAccountTransferToAtm.  # noqa: E501
        :type: ToAccountTransferToAtmKycDocument
        """
        if self._configuration.client_side_validation and kyc_document is None:
            raise ValueError("Invalid value for `kyc_document`, must not be `None`")  # noqa: E501

        self._kyc_document = kyc_document

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
        if issubclass(ToAccountTransferToAtm, dict):
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
        if not isinstance(other, ToAccountTransferToAtm):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ToAccountTransferToAtm):
            return True

        return self.to_dict() != other.to_dict()
