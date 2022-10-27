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


class PostApiCollectionEndpointJson400(object):
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
        'operation_id': 'str'
    }

    attribute_map = {
        'operation_id': 'operation_id'
    }

    def __init__(self, operation_id=None, _configuration=None):  # noqa: E501
        """PostApiCollectionEndpointJson400 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._operation_id = None
        self.discriminator = None

        self.operation_id = operation_id

    @property
    def operation_id(self):
        """Gets the operation_id of this PostApiCollectionEndpointJson400.  # noqa: E501


        :return: The operation_id of this PostApiCollectionEndpointJson400.  # noqa: E501
        :rtype: str
        """
        return self._operation_id

    @operation_id.setter
    def operation_id(self, operation_id):
        """Sets the operation_id of this PostApiCollectionEndpointJson400.


        :param operation_id: The operation_id of this PostApiCollectionEndpointJson400.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and operation_id is None:
            raise ValueError("Invalid value for `operation_id`, must not be `None`")  # noqa: E501

        self._operation_id = operation_id

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
        if issubclass(PostApiCollectionEndpointJson400, dict):
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
        if not isinstance(other, PostApiCollectionEndpointJson400):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostApiCollectionEndpointJson400):
            return True

        return self.to_dict() != other.to_dict()
