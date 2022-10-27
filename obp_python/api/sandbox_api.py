# coding: utf-8

"""
    Open Bank Project API

    An Open Source API for Banks. (c) TESOBE GmbH. 2011 - 2022. Licensed under the AGPL and commercial licences.  # noqa: E501

    OpenAPI spec version: v5.0.0
    Contact: contact@tesobe.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from obp_python.api_client import ApiClient


class SandboxApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def sandbox_data_import(self, body, **kwargs):  # noqa: E501
        """Create sandbox  # noqa: E501

        <p>Import bulk data into the sandbox (Authenticated access).</p><p>This call can be used to create banks, users, accounts and transactions which are stored in the local RDBMS.</p><p>The user needs to have CanCreateSandbox entitlement.</p><p>Note: This is a monolithic call. You could also use a combination of endpoints including create bank, create user, create account and create transaction request to create similar data.</p><p>An example of an import set of data (json) can be found <a href=\"https://raw.githubusercontent.com/OpenBankProject/OBP-API/develop/obp-api/src/main/scala/code/api/sandbox/example_data/2016-04-28/example_import.json\">here</a><br />Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sandbox_data_import(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SandboxDataImport body: SandboxDataImport object that needs to be added. (required)
        :return: SuccessMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.sandbox_data_import_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.sandbox_data_import_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def sandbox_data_import_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create sandbox  # noqa: E501

        <p>Import bulk data into the sandbox (Authenticated access).</p><p>This call can be used to create banks, users, accounts and transactions which are stored in the local RDBMS.</p><p>The user needs to have CanCreateSandbox entitlement.</p><p>Note: This is a monolithic call. You could also use a combination of endpoints including create bank, create user, create account and create transaction request to create similar data.</p><p>An example of an import set of data (json) can be found <a href=\"https://raw.githubusercontent.com/OpenBankProject/OBP-API/develop/obp-api/src/main/scala/code/api/sandbox/example_data/2016-04-28/example_import.json\">here</a><br />Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sandbox_data_import_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SandboxDataImport body: SandboxDataImport object that needs to be added. (required)
        :return: SuccessMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sandbox_data_import" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `sandbox_data_import`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = ['directLogin', 'gatewayLogin']  # noqa: E501

        return self.api_client.call_api(
            '/obp/v5.0.0/sandbox/data-import', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SuccessMessage',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
