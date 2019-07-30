# coding: utf-8

"""
    AVM

    This is api for AVM (automated valuation machine)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: info@enbisys.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PropertyFeatures(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'required_features': 'RequiredFeatures',
        'additional_features': 'AdditionalFeatures'
    }

    attribute_map = {
        'required_features': 'requiredFeatures',
        'additional_features': 'additionalFeatures'
    }

    def __init__(self, required_features=None, additional_features=None):  # noqa: E501
        """PropertyFeatures - a model defined in OpenAPI"""  # noqa: E501

        self._required_features = None
        self._additional_features = None
        self.discriminator = None

        self.required_features = required_features
        if additional_features is not None:
            self.additional_features = additional_features

    @property
    def required_features(self):
        """Gets the required_features of this PropertyFeatures.  # noqa: E501


        :return: The required_features of this PropertyFeatures.  # noqa: E501
        :rtype: RequiredFeatures
        """
        return self._required_features

    @required_features.setter
    def required_features(self, required_features):
        """Sets the required_features of this PropertyFeatures.


        :param required_features: The required_features of this PropertyFeatures.  # noqa: E501
        :type: RequiredFeatures
        """
        if required_features is None:
            raise ValueError("Invalid value for `required_features`, must not be `None`")  # noqa: E501

        self._required_features = required_features

    @property
    def additional_features(self):
        """Gets the additional_features of this PropertyFeatures.  # noqa: E501


        :return: The additional_features of this PropertyFeatures.  # noqa: E501
        :rtype: AdditionalFeatures
        """
        return self._additional_features

    @additional_features.setter
    def additional_features(self, additional_features):
        """Sets the additional_features of this PropertyFeatures.


        :param additional_features: The additional_features of this PropertyFeatures.  # noqa: E501
        :type: AdditionalFeatures
        """

        self._additional_features = additional_features

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PropertyFeatures):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
