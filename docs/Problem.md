# Problem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | A relative URI reference that identifies the problem type. When dereferenced, it SHOULD provide human-readable documentation for the problem type (e.g. using HTML). | [optional] [default to 'about:blank']
**title** | **str** | A short, summary of the problem type. Written in english and readable for engineers (usually not suited for non technical stakeholders and not localized) | [optional] 
**status** | **int** | The HTTP status code generated by the origin server for this occurrence of the problem. | [optional] 
**detail** | **str** | A human-readable explanation specific to this occurrence of the problem | [optional] 
**instance** | **str** | A URI reference that identifies the specific occurrence of the problem. It may or may not yield further information if dereferenced. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


