# coding: utf-8

"""
    LOCKSS Repository Service REST API

    API of the LOCKSS RepositoryService for the LAAWS project  # noqa: E501

    OpenAPI spec version: 1.9
    Contact: dlvargas@stanford.edu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from lockss_repository.api_client import ApiClient


class CollectionsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def collections_collectionid_artifacts_artifactid_delete(self, collectionid, artifactid, **kwargs):  # noqa: E501
        """Remove an artifact from the repository  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.collections_collectionid_artifacts_artifactid_delete(collectionid, artifactid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str collectionid: Collection containing the artifact (required)
        :param str artifactid: Identifier of the artifact (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.collections_collectionid_artifacts_artifactid_delete_with_http_info(collectionid, artifactid, **kwargs)  # noqa: E501
        else:
            (data) = self.collections_collectionid_artifacts_artifactid_delete_with_http_info(collectionid, artifactid, **kwargs)  # noqa: E501
            return data

    def collections_collectionid_artifacts_artifactid_delete_with_http_info(self, collectionid, artifactid, **kwargs):  # noqa: E501
        """Remove an artifact from the repository  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.collections_collectionid_artifacts_artifactid_delete_with_http_info(collectionid, artifactid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str collectionid: Collection containing the artifact (required)
        :param str artifactid: Identifier of the artifact (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['collectionid', 'artifactid']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method collections_collectionid_artifacts_artifactid_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'collectionid' is set
        if ('collectionid' not in params or
                params['collectionid'] is None):
            raise ValueError("Missing the required parameter `collectionid` when calling `collections_collectionid_artifacts_artifactid_delete`")  # noqa: E501
        # verify the required parameter 'artifactid' is set
        if ('artifactid' not in params or
                params['artifactid'] is None):
            raise ValueError("Missing the required parameter `artifactid` when calling `collections_collectionid_artifacts_artifactid_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'collectionid' in params:
            path_params['collectionid'] = params['collectionid']  # noqa: E501
        if 'artifactid' in params:
            path_params['artifactid'] = params['artifactid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/collections/{collectionid}/artifacts/{artifactid}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def collections_collectionid_artifacts_artifactid_get(self, collectionid, artifactid, **kwargs):  # noqa: E501
        """Get artifact content and metadata  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.collections_collectionid_artifacts_artifactid_get(collectionid, artifactid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str collectionid: Collection containing the artifact (required)
        :param str artifactid: Identifier of the artifact (required)
        :param str accept: Content type to return
        :return: StreamingResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.collections_collectionid_artifacts_artifactid_get_with_http_info(collectionid, artifactid, **kwargs)  # noqa: E501
        else:
            (data) = self.collections_collectionid_artifacts_artifactid_get_with_http_info(collectionid, artifactid, **kwargs)  # noqa: E501
            return data

    def collections_collectionid_artifacts_artifactid_get_with_http_info(self, collectionid, artifactid, **kwargs):  # noqa: E501
        """Get artifact content and metadata  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.collections_collectionid_artifacts_artifactid_get_with_http_info(collectionid, artifactid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str collectionid: Collection containing the artifact (required)
        :param str artifactid: Identifier of the artifact (required)
        :param str accept: Content type to return
        :return: StreamingResponseBody
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['collectionid', 'artifactid', 'accept']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method collections_collectionid_artifacts_artifactid_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'collectionid' is set
        if ('collectionid' not in params or
                params['collectionid'] is None):
            raise ValueError("Missing the required parameter `collectionid` when calling `collections_collectionid_artifacts_artifactid_get`")  # noqa: E501
        # verify the required parameter 'artifactid' is set
        if ('artifactid' not in params or
                params['artifactid'] is None):
            raise ValueError("Missing the required parameter `artifactid` when calling `collections_collectionid_artifacts_artifactid_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'collectionid' in params:
            path_params['collectionid'] = params['collectionid']  # noqa: E501
        if 'artifactid' in params:
            path_params['artifactid'] = params['artifactid']  # noqa: E501

        query_params = []

        header_params = {}
        if 'accept' in params:
            header_params['Accept'] = params['accept']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/collections/{collectionid}/artifacts/{artifactid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StreamingResponseBody',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def collections_collectionid_artifacts_artifactid_put(self, collectionid, artifactid, **kwargs):  # noqa: E501
        """Update the committed property of an artifact  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.collections_collectionid_artifacts_artifactid_put(collectionid, artifactid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str collectionid: Collection containing the artifact (required)
        :param str artifactid: Identifier of the artifact (required)
        :param bool committed: New commit status of artifact
        :return: Artifact
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.collections_collectionid_artifacts_artifactid_put_with_http_info(collectionid, artifactid, **kwargs)  # noqa: E501
        else:
            (data) = self.collections_collectionid_artifacts_artifactid_put_with_http_info(collectionid, artifactid, **kwargs)  # noqa: E501
            return data

    def collections_collectionid_artifacts_artifactid_put_with_http_info(self, collectionid, artifactid, **kwargs):  # noqa: E501
        """Update the committed property of an artifact  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.collections_collectionid_artifacts_artifactid_put_with_http_info(collectionid, artifactid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str collectionid: Collection containing the artifact (required)
        :param str artifactid: Identifier of the artifact (required)
        :param bool committed: New commit status of artifact
        :return: Artifact
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['collectionid', 'artifactid', 'committed']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method collections_collectionid_artifacts_artifactid_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'collectionid' is set
        if ('collectionid' not in params or
                params['collectionid'] is None):
            raise ValueError("Missing the required parameter `collectionid` when calling `collections_collectionid_artifacts_artifactid_put`")  # noqa: E501
        # verify the required parameter 'artifactid' is set
        if ('artifactid' not in params or
                params['artifactid'] is None):
            raise ValueError("Missing the required parameter `artifactid` when calling `collections_collectionid_artifacts_artifactid_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'collectionid' in params:
            path_params['collectionid'] = params['collectionid']  # noqa: E501
        if 'artifactid' in params:
            path_params['artifactid'] = params['artifactid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'committed' in params:
            form_params.append(('committed', params['committed']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/collections/{collectionid}/artifacts/{artifactid}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Artifact',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def collections_collectionid_artifacts_post(self, collectionid, auid, uri, content, **kwargs):  # noqa: E501
        """Create an artifact  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.collections_collectionid_artifacts_post(collectionid, auid, uri, content, async=True)
        >>> result = thread.get()

        :param async bool
        :param str collectionid: Collection containing the artifact (required)
        :param str auid: Archival Unit ID (AUID) of new artifact (required)
        :param str uri: URI represented by this artifact (required)
        :param file content: Content byte stream (required)
        :param file aspect_parts: URI aspects represented by this artifact
        :return: Artifact
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.collections_collectionid_artifacts_post_with_http_info(collectionid, auid, uri, content, **kwargs)  # noqa: E501
        else:
            (data) = self.collections_collectionid_artifacts_post_with_http_info(collectionid, auid, uri, content, **kwargs)  # noqa: E501
            return data

    def collections_collectionid_artifacts_post_with_http_info(self, collectionid, auid, uri, content, **kwargs):  # noqa: E501
        """Create an artifact  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.collections_collectionid_artifacts_post_with_http_info(collectionid, auid, uri, content, async=True)
        >>> result = thread.get()

        :param async bool
        :param str collectionid: Collection containing the artifact (required)
        :param str auid: Archival Unit ID (AUID) of new artifact (required)
        :param str uri: URI represented by this artifact (required)
        :param file content: Content byte stream (required)
        :param file aspect_parts: URI aspects represented by this artifact
        :return: Artifact
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['collectionid', 'auid', 'uri', 'content', 'aspect_parts']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method collections_collectionid_artifacts_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'collectionid' is set
        if ('collectionid' not in params or
                params['collectionid'] is None):
            raise ValueError("Missing the required parameter `collectionid` when calling `collections_collectionid_artifacts_post`")  # noqa: E501
        # verify the required parameter 'auid' is set
        if ('auid' not in params or
                params['auid'] is None):
            raise ValueError("Missing the required parameter `auid` when calling `collections_collectionid_artifacts_post`")  # noqa: E501
        # verify the required parameter 'uri' is set
        if ('uri' not in params or
                params['uri'] is None):
            raise ValueError("Missing the required parameter `uri` when calling `collections_collectionid_artifacts_post`")  # noqa: E501
        # verify the required parameter 'content' is set
        if ('content' not in params or
                params['content'] is None):
            raise ValueError("Missing the required parameter `content` when calling `collections_collectionid_artifacts_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'collectionid' in params:
            path_params['collectionid'] = params['collectionid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'auid' in params:
            form_params.append(('auid', params['auid']))  # noqa: E501
        if 'uri' in params:
            form_params.append(('uri', params['uri']))  # noqa: E501
        if 'content' in params:
            local_var_files['content'] = params['content']  # noqa: E501
        if 'aspect_parts' in params:
            local_var_files['aspectParts'] = params['aspect_parts']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/collections/{collectionid}/artifacts', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Artifact',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def collections_collectionid_aus_auid_artifacts_get(self, collectionid, auid, **kwargs):  # noqa: E501
        """Get committed artifacts in a collection and Archival Unit  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.collections_collectionid_aus_auid_artifacts_get(collectionid, auid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str collectionid: Identifier of the collection containing the artifacts (required)
        :param str auid: Identifier of the Archival Unit containing the artifacts (required)
        :param str url: The URL contained by the artifacts
        :param str url_prefix: The prefix to be matched by the artifact URLs
        :param str version: The version of the URL contained by the artifacts
        :return: list[Artifact]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.collections_collectionid_aus_auid_artifacts_get_with_http_info(collectionid, auid, **kwargs)  # noqa: E501
        else:
            (data) = self.collections_collectionid_aus_auid_artifacts_get_with_http_info(collectionid, auid, **kwargs)  # noqa: E501
            return data

    def collections_collectionid_aus_auid_artifacts_get_with_http_info(self, collectionid, auid, **kwargs):  # noqa: E501
        """Get committed artifacts in a collection and Archival Unit  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.collections_collectionid_aus_auid_artifacts_get_with_http_info(collectionid, auid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str collectionid: Identifier of the collection containing the artifacts (required)
        :param str auid: Identifier of the Archival Unit containing the artifacts (required)
        :param str url: The URL contained by the artifacts
        :param str url_prefix: The prefix to be matched by the artifact URLs
        :param str version: The version of the URL contained by the artifacts
        :return: list[Artifact]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['collectionid', 'auid', 'url', 'url_prefix', 'version']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method collections_collectionid_aus_auid_artifacts_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'collectionid' is set
        if ('collectionid' not in params or
                params['collectionid'] is None):
            raise ValueError("Missing the required parameter `collectionid` when calling `collections_collectionid_aus_auid_artifacts_get`")  # noqa: E501
        # verify the required parameter 'auid' is set
        if ('auid' not in params or
                params['auid'] is None):
            raise ValueError("Missing the required parameter `auid` when calling `collections_collectionid_aus_auid_artifacts_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'collectionid' in params:
            path_params['collectionid'] = params['collectionid']  # noqa: E501
        if 'auid' in params:
            path_params['auid'] = params['auid']  # noqa: E501

        query_params = []
        if 'url' in params:
            query_params.append(('url', params['url']))  # noqa: E501
        if 'url_prefix' in params:
            query_params.append(('urlPrefix', params['url_prefix']))  # noqa: E501
        if 'version' in params:
            query_params.append(('version', params['version']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/collections/{collectionid}/aus/{auid}/artifacts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Artifact]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def collections_collectionid_aus_auid_size_get(self, collectionid, auid, **kwargs):  # noqa: E501
        """Get the size of Archival Unit artifacts in a collection  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.collections_collectionid_aus_auid_size_get(collectionid, auid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str collectionid: Identifier of the collection containing the artifacts (required)
        :param str auid: Identifier of the Archival Unit containing the artifacts (required)
        :param str url: The URL contained by the artifacts
        :param str url_prefix: The prefix to be matched by the artifact URLs
        :param str version: The version of the URL contained by the artifacts
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.collections_collectionid_aus_auid_size_get_with_http_info(collectionid, auid, **kwargs)  # noqa: E501
        else:
            (data) = self.collections_collectionid_aus_auid_size_get_with_http_info(collectionid, auid, **kwargs)  # noqa: E501
            return data

    def collections_collectionid_aus_auid_size_get_with_http_info(self, collectionid, auid, **kwargs):  # noqa: E501
        """Get the size of Archival Unit artifacts in a collection  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.collections_collectionid_aus_auid_size_get_with_http_info(collectionid, auid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str collectionid: Identifier of the collection containing the artifacts (required)
        :param str auid: Identifier of the Archival Unit containing the artifacts (required)
        :param str url: The URL contained by the artifacts
        :param str url_prefix: The prefix to be matched by the artifact URLs
        :param str version: The version of the URL contained by the artifacts
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['collectionid', 'auid', 'url', 'url_prefix', 'version']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method collections_collectionid_aus_auid_size_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'collectionid' is set
        if ('collectionid' not in params or
                params['collectionid'] is None):
            raise ValueError("Missing the required parameter `collectionid` when calling `collections_collectionid_aus_auid_size_get`")  # noqa: E501
        # verify the required parameter 'auid' is set
        if ('auid' not in params or
                params['auid'] is None):
            raise ValueError("Missing the required parameter `auid` when calling `collections_collectionid_aus_auid_size_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'collectionid' in params:
            path_params['collectionid'] = params['collectionid']  # noqa: E501
        if 'auid' in params:
            path_params['auid'] = params['auid']  # noqa: E501

        query_params = []
        if 'url' in params:
            query_params.append(('url', params['url']))  # noqa: E501
        if 'url_prefix' in params:
            query_params.append(('urlPrefix', params['url_prefix']))  # noqa: E501
        if 'version' in params:
            query_params.append(('version', params['version']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/collections/{collectionid}/aus/{auid}/size', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='int',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def collections_collectionid_aus_get(self, collectionid, **kwargs):  # noqa: E501
        """Get Archival Unit IDs (AUIDs) in a collection  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.collections_collectionid_aus_get(collectionid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str collectionid: Identifier of the collection containing the Archival Units (required)
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.collections_collectionid_aus_get_with_http_info(collectionid, **kwargs)  # noqa: E501
        else:
            (data) = self.collections_collectionid_aus_get_with_http_info(collectionid, **kwargs)  # noqa: E501
            return data

    def collections_collectionid_aus_get_with_http_info(self, collectionid, **kwargs):  # noqa: E501
        """Get Archival Unit IDs (AUIDs) in a collection  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.collections_collectionid_aus_get_with_http_info(collectionid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str collectionid: Identifier of the collection containing the Archival Units (required)
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['collectionid']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method collections_collectionid_aus_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'collectionid' is set
        if ('collectionid' not in params or
                params['collectionid'] is None):
            raise ValueError("Missing the required parameter `collectionid` when calling `collections_collectionid_aus_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'collectionid' in params:
            path_params['collectionid'] = params['collectionid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/collections/{collectionid}/aus', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def collections_get(self, **kwargs):  # noqa: E501
        """Get collection identifiers of the committed artifacts in the repository  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.collections_get(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.collections_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.collections_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def collections_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get collection identifiers of the committed artifacts in the repository  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.collections_get_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method collections_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/collections', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
