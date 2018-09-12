# lockss_repository.CollectionsApi

All URIs are relative to *http://laaws.lockss.org:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**collections_collectionid_artifacts_artifactid_delete**](CollectionsApi.md#collections_collectionid_artifacts_artifactid_delete) | **DELETE** /collections/{collectionid}/artifacts/{artifactid} | Remove an artifact from the repository
[**collections_collectionid_artifacts_artifactid_get**](CollectionsApi.md#collections_collectionid_artifacts_artifactid_get) | **GET** /collections/{collectionid}/artifacts/{artifactid} | Get artifact content and metadata
[**collections_collectionid_artifacts_artifactid_put**](CollectionsApi.md#collections_collectionid_artifacts_artifactid_put) | **PUT** /collections/{collectionid}/artifacts/{artifactid} | Update the committed property of an artifact
[**collections_collectionid_artifacts_post**](CollectionsApi.md#collections_collectionid_artifacts_post) | **POST** /collections/{collectionid}/artifacts | Create an artifact
[**collections_collectionid_aus_auid_artifacts_get**](CollectionsApi.md#collections_collectionid_aus_auid_artifacts_get) | **GET** /collections/{collectionid}/aus/{auid}/artifacts | Get committed artifacts in a collection and Archival Unit
[**collections_collectionid_aus_auid_size_get**](CollectionsApi.md#collections_collectionid_aus_auid_size_get) | **GET** /collections/{collectionid}/aus/{auid}/size | Get the size of Archival Unit artifacts in a collection
[**collections_collectionid_aus_get**](CollectionsApi.md#collections_collectionid_aus_get) | **GET** /collections/{collectionid}/aus | Get Archival Unit IDs (AUIDs) in a collection
[**collections_get**](CollectionsApi.md#collections_get) | **GET** /collections | Get collection identifiers of the committed artifacts in the repository


# **collections_collectionid_artifacts_artifactid_delete**
> collections_collectionid_artifacts_artifactid_delete(collectionid, artifactid)

Remove an artifact from the repository

### Example
```python
from __future__ import print_function
import time
import lockss_repository
from lockss_repository.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lockss_repository.CollectionsApi()
collectionid = 'collectionid_example' # str | Collection containing the artifact
artifactid = 'artifactid_example' # str | Identifier of the artifact

try:
    # Remove an artifact from the repository
    api_instance.collections_collectionid_artifacts_artifactid_delete(collectionid, artifactid)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_collectionid_artifacts_artifactid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collectionid** | **str**| Collection containing the artifact | 
 **artifactid** | **str**| Identifier of the artifact | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collectionid_artifacts_artifactid_get**
> StreamingResponseBody collections_collectionid_artifacts_artifactid_get(collectionid, artifactid, accept=accept)

Get artifact content and metadata

### Example
```python
from __future__ import print_function
import time
import lockss_repository
from lockss_repository.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lockss_repository.CollectionsApi()
collectionid = 'collectionid_example' # str | Collection containing the artifact
artifactid = 'artifactid_example' # str | Identifier of the artifact
accept = 'multipart/related' # str | Content type to return (optional) (default to multipart/related)

try:
    # Get artifact content and metadata
    api_response = api_instance.collections_collectionid_artifacts_artifactid_get(collectionid, artifactid, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_collectionid_artifacts_artifactid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collectionid** | **str**| Collection containing the artifact | 
 **artifactid** | **str**| Identifier of the artifact | 
 **accept** | **str**| Content type to return | [optional] [default to multipart/related]

### Return type

[**StreamingResponseBody**](StreamingResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collectionid_artifacts_artifactid_put**
> Artifact collections_collectionid_artifacts_artifactid_put(collectionid, artifactid, committed=committed)

Update the committed property of an artifact

### Example
```python
from __future__ import print_function
import time
import lockss_repository
from lockss_repository.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lockss_repository.CollectionsApi()
collectionid = 'collectionid_example' # str | Collection containing the artifact
artifactid = 'artifactid_example' # str | Identifier of the artifact
committed = true # bool | New commit status of artifact (optional)

try:
    # Update the committed property of an artifact
    api_response = api_instance.collections_collectionid_artifacts_artifactid_put(collectionid, artifactid, committed=committed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_collectionid_artifacts_artifactid_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collectionid** | **str**| Collection containing the artifact | 
 **artifactid** | **str**| Identifier of the artifact | 
 **committed** | **bool**| New commit status of artifact | [optional] 

### Return type

[**Artifact**](Artifact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collectionid_artifacts_post**
> Artifact collections_collectionid_artifacts_post(collectionid, auid, uri, content, aspect_parts=aspect_parts)

Create an artifact

### Example
```python
from __future__ import print_function
import time
import lockss_repository
from lockss_repository.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lockss_repository.CollectionsApi()
collectionid = 'collectionid_example' # str | Collection containing the artifact
auid = 'auid_example' # str | Archival Unit ID (AUID) of new artifact
uri = 'uri_example' # str | URI represented by this artifact
content = '/path/to/file.txt' # file | Content byte stream
aspect_parts = '/path/to/file.txt' # file | URI aspects represented by this artifact (optional)

try:
    # Create an artifact
    api_response = api_instance.collections_collectionid_artifacts_post(collectionid, auid, uri, content, aspect_parts=aspect_parts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_collectionid_artifacts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collectionid** | **str**| Collection containing the artifact | 
 **auid** | **str**| Archival Unit ID (AUID) of new artifact | 
 **uri** | **str**| URI represented by this artifact | 
 **content** | **file**| Content byte stream | 
 **aspect_parts** | **file**| URI aspects represented by this artifact | [optional] 

### Return type

[**Artifact**](Artifact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collectionid_aus_auid_artifacts_get**
> list[Artifact] collections_collectionid_aus_auid_artifacts_get(collectionid, auid, url=url, url_prefix=url_prefix, version=version)

Get committed artifacts in a collection and Archival Unit

### Example
```python
from __future__ import print_function
import time
import lockss_repository
from lockss_repository.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lockss_repository.CollectionsApi()
collectionid = 'collectionid_example' # str | Identifier of the collection containing the artifacts
auid = 'auid_example' # str | Identifier of the Archival Unit containing the artifacts
url = 'url_example' # str | The URL contained by the artifacts (optional)
url_prefix = 'url_prefix_example' # str | The prefix to be matched by the artifact URLs (optional)
version = 'version_example' # str | The version of the URL contained by the artifacts (optional)

try:
    # Get committed artifacts in a collection and Archival Unit
    api_response = api_instance.collections_collectionid_aus_auid_artifacts_get(collectionid, auid, url=url, url_prefix=url_prefix, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_collectionid_aus_auid_artifacts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collectionid** | **str**| Identifier of the collection containing the artifacts | 
 **auid** | **str**| Identifier of the Archival Unit containing the artifacts | 
 **url** | **str**| The URL contained by the artifacts | [optional] 
 **url_prefix** | **str**| The prefix to be matched by the artifact URLs | [optional] 
 **version** | **str**| The version of the URL contained by the artifacts | [optional] 

### Return type

[**list[Artifact]**](Artifact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collectionid_aus_auid_size_get**
> int collections_collectionid_aus_auid_size_get(collectionid, auid, url=url, url_prefix=url_prefix, version=version)

Get the size of Archival Unit artifacts in a collection

### Example
```python
from __future__ import print_function
import time
import lockss_repository
from lockss_repository.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lockss_repository.CollectionsApi()
collectionid = 'collectionid_example' # str | Identifier of the collection containing the artifacts
auid = 'auid_example' # str | Identifier of the Archival Unit containing the artifacts
url = 'url_example' # str | The URL contained by the artifacts (optional)
url_prefix = 'url_prefix_example' # str | The prefix to be matched by the artifact URLs (optional)
version = 'version_example' # str | The version of the URL contained by the artifacts (optional)

try:
    # Get the size of Archival Unit artifacts in a collection
    api_response = api_instance.collections_collectionid_aus_auid_size_get(collectionid, auid, url=url, url_prefix=url_prefix, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_collectionid_aus_auid_size_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collectionid** | **str**| Identifier of the collection containing the artifacts | 
 **auid** | **str**| Identifier of the Archival Unit containing the artifacts | 
 **url** | **str**| The URL contained by the artifacts | [optional] 
 **url_prefix** | **str**| The prefix to be matched by the artifact URLs | [optional] 
 **version** | **str**| The version of the URL contained by the artifacts | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_collectionid_aus_get**
> list[str] collections_collectionid_aus_get(collectionid)

Get Archival Unit IDs (AUIDs) in a collection

### Example
```python
from __future__ import print_function
import time
import lockss_repository
from lockss_repository.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lockss_repository.CollectionsApi()
collectionid = 'collectionid_example' # str | Identifier of the collection containing the Archival Units

try:
    # Get Archival Unit IDs (AUIDs) in a collection
    api_response = api_instance.collections_collectionid_aus_get(collectionid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_collectionid_aus_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collectionid** | **str**| Identifier of the collection containing the Archival Units | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_get**
> list[str] collections_get()

Get collection identifiers of the committed artifacts in the repository

### Example
```python
from __future__ import print_function
import time
import lockss_repository
from lockss_repository.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lockss_repository.CollectionsApi()

try:
    # Get collection identifiers of the committed artifacts in the repository
    api_response = api_instance.collections_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->collections_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

