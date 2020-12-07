# swagger_client.DefaultApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**process_doc**](DefaultApi.md#process_doc) | **POST** /actions/process/doc | Process new doc
[**process_msg**](DefaultApi.md#process_msg) | **POST** /actions/process/msg | Process new msg
[**rank_entities**](DefaultApi.md#rank_entities) | **POST** /actions/rank | Rank Entities


# **process_doc**
> process_doc(body)

Process new doc



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.ProcessDocRequest() # ProcessDocRequest | Doc object that needs to be processed

try:
    # Process new doc
    api_instance.process_doc(body)
except ApiException as e:
    print("Exception when calling DefaultApi->process_doc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProcessDocRequest**](ProcessDocRequest.md)| Doc object that needs to be processed | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_msg**
> process_msg(body)

Process new msg



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.ProcessMsgRequest() # ProcessMsgRequest | Doc object that needs to be processed

try:
    # Process new msg
    api_instance.process_msg(body)
except ApiException as e:
    print("Exception when calling DefaultApi->process_msg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProcessMsgRequest**](ProcessMsgRequest.md)| Doc object that needs to be processed | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rank_entities**
> RankEntitiesResponse rank_entities(body)

Rank Entities



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.RankEntitiesRequest() # RankEntitiesRequest | Rank arguments

try:
    # Rank Entities
    api_response = api_instance.rank_entities(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->rank_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RankEntitiesRequest**](RankEntitiesRequest.md)| Rank arguments | 

### Return type

[**RankEntitiesResponse**](RankEntitiesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

