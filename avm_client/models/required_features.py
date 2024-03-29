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


class RequiredFeatures(object):
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
        'postcode': 'str',
        'new_or_resale': 'NewOrResale',
        'floor_level': 'FloorLevel',
        'total_floor_area_in_sqf': 'int',
        'property_type': 'PropertyType',
        'number_of_rooms': 'int'
    }

    attribute_map = {
        'postcode': 'postcode',
        'new_or_resale': 'newOrResale',
        'floor_level': 'floorLevel',
        'total_floor_area_in_sqf': 'totalFloorAreaInSqf',
        'property_type': 'propertyType',
        'number_of_rooms': 'numberOfRooms'
    }

    def __init__(self, postcode=None, new_or_resale=None, floor_level=None, total_floor_area_in_sqf=None, property_type=None, number_of_rooms=None):  # noqa: E501
        """RequiredFeatures - a model defined in OpenAPI"""  # noqa: E501

        self._postcode = None
        self._new_or_resale = None
        self._floor_level = None
        self._total_floor_area_in_sqf = None
        self._property_type = None
        self._number_of_rooms = None
        self.discriminator = None

        self.postcode = postcode
        self.new_or_resale = new_or_resale
        self.floor_level = floor_level
        self.total_floor_area_in_sqf = total_floor_area_in_sqf
        self.property_type = property_type
        self.number_of_rooms = number_of_rooms

    @property
    def postcode(self):
        """Gets the postcode of this RequiredFeatures.  # noqa: E501

        Postcode  # noqa: E501

        :return: The postcode of this RequiredFeatures.  # noqa: E501
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """Sets the postcode of this RequiredFeatures.

        Postcode  # noqa: E501

        :param postcode: The postcode of this RequiredFeatures.  # noqa: E501
        :type: str
        """
        if postcode is None:
            raise ValueError("Invalid value for `postcode`, must not be `None`")  # noqa: E501

        self._postcode = postcode

    @property
    def new_or_resale(self):
        """Gets the new_or_resale of this RequiredFeatures.  # noqa: E501


        :return: The new_or_resale of this RequiredFeatures.  # noqa: E501
        :rtype: NewOrResale
        """
        return self._new_or_resale

    @new_or_resale.setter
    def new_or_resale(self, new_or_resale):
        """Sets the new_or_resale of this RequiredFeatures.


        :param new_or_resale: The new_or_resale of this RequiredFeatures.  # noqa: E501
        :type: NewOrResale
        """
        if new_or_resale is None:
            raise ValueError("Invalid value for `new_or_resale`, must not be `None`")  # noqa: E501

        self._new_or_resale = new_or_resale

    @property
    def floor_level(self):
        """Gets the floor_level of this RequiredFeatures.  # noqa: E501


        :return: The floor_level of this RequiredFeatures.  # noqa: E501
        :rtype: FloorLevel
        """
        return self._floor_level

    @floor_level.setter
    def floor_level(self, floor_level):
        """Sets the floor_level of this RequiredFeatures.


        :param floor_level: The floor_level of this RequiredFeatures.  # noqa: E501
        :type: FloorLevel
        """
        if floor_level is None:
            raise ValueError("Invalid value for `floor_level`, must not be `None`")  # noqa: E501

        self._floor_level = floor_level

    @property
    def total_floor_area_in_sqf(self):
        """Gets the total_floor_area_in_sqf of this RequiredFeatures.  # noqa: E501

        Floor area (sqf)  # noqa: E501

        :return: The total_floor_area_in_sqf of this RequiredFeatures.  # noqa: E501
        :rtype: int
        """
        return self._total_floor_area_in_sqf

    @total_floor_area_in_sqf.setter
    def total_floor_area_in_sqf(self, total_floor_area_in_sqf):
        """Sets the total_floor_area_in_sqf of this RequiredFeatures.

        Floor area (sqf)  # noqa: E501

        :param total_floor_area_in_sqf: The total_floor_area_in_sqf of this RequiredFeatures.  # noqa: E501
        :type: int
        """
        if total_floor_area_in_sqf is None:
            raise ValueError("Invalid value for `total_floor_area_in_sqf`, must not be `None`")  # noqa: E501
        if total_floor_area_in_sqf is not None and total_floor_area_in_sqf > 10000:  # noqa: E501
            raise ValueError("Invalid value for `total_floor_area_in_sqf`, must be a value less than or equal to `10000`")  # noqa: E501
        if total_floor_area_in_sqf is not None and total_floor_area_in_sqf < 50:  # noqa: E501
            raise ValueError("Invalid value for `total_floor_area_in_sqf`, must be a value greater than or equal to `50`")  # noqa: E501

        self._total_floor_area_in_sqf = total_floor_area_in_sqf

    @property
    def property_type(self):
        """Gets the property_type of this RequiredFeatures.  # noqa: E501


        :return: The property_type of this RequiredFeatures.  # noqa: E501
        :rtype: PropertyType
        """
        return self._property_type

    @property_type.setter
    def property_type(self, property_type):
        """Sets the property_type of this RequiredFeatures.


        :param property_type: The property_type of this RequiredFeatures.  # noqa: E501
        :type: PropertyType
        """
        if property_type is None:
            raise ValueError("Invalid value for `property_type`, must not be `None`")  # noqa: E501

        self._property_type = property_type

    @property
    def number_of_rooms(self):
        """Gets the number_of_rooms of this RequiredFeatures.  # noqa: E501


        :return: The number_of_rooms of this RequiredFeatures.  # noqa: E501
        :rtype: int
        """
        return self._number_of_rooms

    @number_of_rooms.setter
    def number_of_rooms(self, number_of_rooms):
        """Sets the number_of_rooms of this RequiredFeatures.


        :param number_of_rooms: The number_of_rooms of this RequiredFeatures.  # noqa: E501
        :type: int
        """
        if number_of_rooms is None:
            raise ValueError("Invalid value for `number_of_rooms`, must not be `None`")  # noqa: E501
        if number_of_rooms is not None and number_of_rooms > 9:  # noqa: E501
            raise ValueError("Invalid value for `number_of_rooms`, must be a value less than or equal to `9`")  # noqa: E501
        if number_of_rooms is not None and number_of_rooms < 1:  # noqa: E501
            raise ValueError("Invalid value for `number_of_rooms`, must be a value greater than or equal to `1`")  # noqa: E501

        self._number_of_rooms = number_of_rooms

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
        if not isinstance(other, RequiredFeatures):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
