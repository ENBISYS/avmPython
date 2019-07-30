# avm.DefaultApi

All URIs are relative to *https://avm.enbisys.com/api/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_fast_valuation**](DefaultApi.md#get_fast_valuation) | **POST** /properties/getFastValuation | 
[**get_valuation**](DefaultApi.md#get_valuation) | **POST** /properties/getValuation | 


# **get_fast_valuation**
> int get_fast_valuation(property_features)



Get only property price valuation without confidence estimation

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_features** | [**PropertyFeatures**](PropertyFeatures.md)| Property features that describe property | 

### Return type

**int**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully done |  -  |
**400** | Bad request |  -  |
**402** | Payment Required |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method not allowed |  -  |
**415** | Unsupported media type |  -  |
**429** | Too many request |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **get_valuation**
> Valuation get_valuation(property_features)

Get property price valuation with confidence estimation

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property_features** | [**PropertyFeatures**](PropertyFeatures.md)| Property features to valuate | 

### Return type

[**Valuation**](Valuation.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successfully done |  -  |
**400** | Bad request |  -  |
**402** | Payment Required |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method not allowed |  -  |
**415** | Unsupported media type |  -  |
**429** | Too many request |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

