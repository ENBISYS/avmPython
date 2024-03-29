# Python API client for AVM

This is api client library for AVM (automated valuation machine) - https://avm.enbisys.com/

Get instant and accurate Property Valuations and Predictive Analytics with our AI and Big Data tools. And make smart decisions faster

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

```sh
pip install avm_client
```

Then import the package:
```python
import avm_client
```

## Getting Started

```python
from __future__ import print_function
import avm_client
from pprint import pprint
from avm_client import (
    FloorLevel,
    NewOrResale,
    PropertyType,
    LeaseholdOrFreehold,
)
from avm_client.rest import ApiException

configuration = avm_client.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['X-API-KEY'] = 'SET YOUR TOKEN HERE!'
configuration.host = "https://avm.enbisys.com/api"

# Create an instance of the API class
api_instance = avm_client.DefaultApi(avm_client.ApiClient(configuration))

required_features = avm_client.RequiredFeatures(
    postcode="B1 1TB",
    new_or_resale=NewOrResale.NEW,
    floor_level=FloorLevel.FLOOR_3,
    total_floor_area_in_sqf=143,
    property_type=PropertyType.DETACHED_HOUSE,
    number_of_rooms=3,
)

additional_features = avm_client.AdditionalFeatures(
    price_of_previous_sale=500000,
    date_of_previous_sale="2019-03-04",
    leasehold_or_freehold=LeaseholdOrFreehold.FREEHOLD,
)

property_features = avm_client.PropertyFeatures(required_features, additional_features)

try:
    price = api_instance.get_fast_valuation(property_features)
    valuation = api_instance.get_valuation(property_features)

    pprint(price)
    pprint(valuation)

except ApiException as e:
    print("Exception when calling DefaultApi->get_fast_valuation: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://avm.enbisys.com/api/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**get_fast_valuation**](docs/DefaultApi.md#get_fast_valuation) | **POST** /properties/getFastValuation | 
*DefaultApi* | [**get_valuation**](docs/DefaultApi.md#get_valuation) | **POST** /properties/getValuation | 


## Documentation For Models

 - [AdditionalFeatures](docs/AdditionalFeatures.md)
 - [BuiltForm](docs/BuiltForm.md)
 - [EnergyEfficiency](docs/EnergyEfficiency.md)
 - [EnergyRating](docs/EnergyRating.md)
 - [FloorLevel](docs/FloorLevel.md)
 - [LeaseholdOrFreehold](docs/LeaseholdOrFreehold.md)
 - [NewOrResale](docs/NewOrResale.md)
 - [Problem](docs/Problem.md)
 - [PropertyFeatures](docs/PropertyFeatures.md)
 - [PropertyType](docs/PropertyType.md)
 - [RequiredFeatures](docs/RequiredFeatures.md)
 - [RoofInsulation](docs/RoofInsulation.md)
 - [RoofType](docs/RoofType.md)
 - [Valuation](docs/Valuation.md)
 - [ValuationPriceDistribution](docs/ValuationPriceDistribution.md)
 - [WallInsulation](docs/WallInsulation.md)
 - [WallType](docs/WallType.md)
 - [WindowGlazingType](docs/WindowGlazingType.md)


## Documentation For Authorization


## ApiKeyAuth

- **Type**: API key
- **API key parameter name**: X-API-KEY
- **Location**: HTTP header


## Author

enbisys.com
