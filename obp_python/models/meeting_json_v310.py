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


class MeetingJsonV310(object):
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
        'present': 'MeetingPresentJson',
        'provider_id': 'str',
        'creator': 'ContactDetailsJson',
        'invitees': 'list[InviteeJson]',
        'bank_id': 'str',
        'purpose_id': 'str',
        'when': 'date',
        'meeting_id': 'str',
        'keys': 'MeetingKeysJson'
    }

    attribute_map = {
        'present': 'present',
        'provider_id': 'provider_id',
        'creator': 'creator',
        'invitees': 'invitees',
        'bank_id': 'bank_id',
        'purpose_id': 'purpose_id',
        'when': 'when',
        'meeting_id': 'meeting_id',
        'keys': 'keys'
    }

    def __init__(self, present=None, provider_id=None, creator=None, invitees=None, bank_id=None, purpose_id=None, when=None, meeting_id=None, keys=None, _configuration=None):  # noqa: E501
        """MeetingJsonV310 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._present = None
        self._provider_id = None
        self._creator = None
        self._invitees = None
        self._bank_id = None
        self._purpose_id = None
        self._when = None
        self._meeting_id = None
        self._keys = None
        self.discriminator = None

        self.present = present
        self.provider_id = provider_id
        self.creator = creator
        self.invitees = invitees
        self.bank_id = bank_id
        self.purpose_id = purpose_id
        self.when = when
        self.meeting_id = meeting_id
        self.keys = keys

    @property
    def present(self):
        """Gets the present of this MeetingJsonV310.  # noqa: E501


        :return: The present of this MeetingJsonV310.  # noqa: E501
        :rtype: MeetingPresentJson
        """
        return self._present

    @present.setter
    def present(self, present):
        """Sets the present of this MeetingJsonV310.


        :param present: The present of this MeetingJsonV310.  # noqa: E501
        :type: MeetingPresentJson
        """
        if self._configuration.client_side_validation and present is None:
            raise ValueError("Invalid value for `present`, must not be `None`")  # noqa: E501

        self._present = present

    @property
    def provider_id(self):
        """Gets the provider_id of this MeetingJsonV310.  # noqa: E501


        :return: The provider_id of this MeetingJsonV310.  # noqa: E501
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this MeetingJsonV310.


        :param provider_id: The provider_id of this MeetingJsonV310.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and provider_id is None:
            raise ValueError("Invalid value for `provider_id`, must not be `None`")  # noqa: E501

        self._provider_id = provider_id

    @property
    def creator(self):
        """Gets the creator of this MeetingJsonV310.  # noqa: E501


        :return: The creator of this MeetingJsonV310.  # noqa: E501
        :rtype: ContactDetailsJson
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this MeetingJsonV310.


        :param creator: The creator of this MeetingJsonV310.  # noqa: E501
        :type: ContactDetailsJson
        """
        if self._configuration.client_side_validation and creator is None:
            raise ValueError("Invalid value for `creator`, must not be `None`")  # noqa: E501

        self._creator = creator

    @property
    def invitees(self):
        """Gets the invitees of this MeetingJsonV310.  # noqa: E501


        :return: The invitees of this MeetingJsonV310.  # noqa: E501
        :rtype: list[InviteeJson]
        """
        return self._invitees

    @invitees.setter
    def invitees(self, invitees):
        """Sets the invitees of this MeetingJsonV310.


        :param invitees: The invitees of this MeetingJsonV310.  # noqa: E501
        :type: list[InviteeJson]
        """
        if self._configuration.client_side_validation and invitees is None:
            raise ValueError("Invalid value for `invitees`, must not be `None`")  # noqa: E501

        self._invitees = invitees

    @property
    def bank_id(self):
        """Gets the bank_id of this MeetingJsonV310.  # noqa: E501


        :return: The bank_id of this MeetingJsonV310.  # noqa: E501
        :rtype: str
        """
        return self._bank_id

    @bank_id.setter
    def bank_id(self, bank_id):
        """Sets the bank_id of this MeetingJsonV310.


        :param bank_id: The bank_id of this MeetingJsonV310.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and bank_id is None:
            raise ValueError("Invalid value for `bank_id`, must not be `None`")  # noqa: E501

        self._bank_id = bank_id

    @property
    def purpose_id(self):
        """Gets the purpose_id of this MeetingJsonV310.  # noqa: E501


        :return: The purpose_id of this MeetingJsonV310.  # noqa: E501
        :rtype: str
        """
        return self._purpose_id

    @purpose_id.setter
    def purpose_id(self, purpose_id):
        """Sets the purpose_id of this MeetingJsonV310.


        :param purpose_id: The purpose_id of this MeetingJsonV310.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and purpose_id is None:
            raise ValueError("Invalid value for `purpose_id`, must not be `None`")  # noqa: E501

        self._purpose_id = purpose_id

    @property
    def when(self):
        """Gets the when of this MeetingJsonV310.  # noqa: E501


        :return: The when of this MeetingJsonV310.  # noqa: E501
        :rtype: date
        """
        return self._when

    @when.setter
    def when(self, when):
        """Sets the when of this MeetingJsonV310.


        :param when: The when of this MeetingJsonV310.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and when is None:
            raise ValueError("Invalid value for `when`, must not be `None`")  # noqa: E501

        self._when = when

    @property
    def meeting_id(self):
        """Gets the meeting_id of this MeetingJsonV310.  # noqa: E501


        :return: The meeting_id of this MeetingJsonV310.  # noqa: E501
        :rtype: str
        """
        return self._meeting_id

    @meeting_id.setter
    def meeting_id(self, meeting_id):
        """Sets the meeting_id of this MeetingJsonV310.


        :param meeting_id: The meeting_id of this MeetingJsonV310.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and meeting_id is None:
            raise ValueError("Invalid value for `meeting_id`, must not be `None`")  # noqa: E501

        self._meeting_id = meeting_id

    @property
    def keys(self):
        """Gets the keys of this MeetingJsonV310.  # noqa: E501


        :return: The keys of this MeetingJsonV310.  # noqa: E501
        :rtype: MeetingKeysJson
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        """Sets the keys of this MeetingJsonV310.


        :param keys: The keys of this MeetingJsonV310.  # noqa: E501
        :type: MeetingKeysJson
        """
        if self._configuration.client_side_validation and keys is None:
            raise ValueError("Invalid value for `keys`, must not be `None`")  # noqa: E501

        self._keys = keys

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
        if issubclass(MeetingJsonV310, dict):
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
        if not isinstance(other, MeetingJsonV310):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MeetingJsonV310):
            return True

        return self.to_dict() != other.to_dict()
