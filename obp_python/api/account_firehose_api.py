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


class AccountFirehoseApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_fast_firehose_accounts_at_one_bank(self, bank_id, **kwargs):  # noqa: E501
        """Get Fast Firehose Accounts at Bank  # noqa: E501

        <p>This endpoint allows bulk access to accounts.</p><p>optional pagination parameters for filter with accounts</p><p>Possible custom url parameters for pagination:</p><ul><li>limit=NUMBER ==&gt; default value: 50</li><li>offset=NUMBER ==&gt; default value: 0</li></ul><p>eg1:?limit=100&amp;offset=0</p><ul><li>sort_direction=ASC/DESC ==&gt; default value: DESC.</li></ul><p>eg2:?limit=100&amp;offset=0&amp;sort_direction=ASC</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_fast_firehose_accounts_at_one_bank(bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bank_id: The bank id (required)
        :return: FastFirehoseAccountsJsonV400
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_fast_firehose_accounts_at_one_bank_with_http_info(bank_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_fast_firehose_accounts_at_one_bank_with_http_info(bank_id, **kwargs)  # noqa: E501
            return data

    def get_fast_firehose_accounts_at_one_bank_with_http_info(self, bank_id, **kwargs):  # noqa: E501
        """Get Fast Firehose Accounts at Bank  # noqa: E501

        <p>This endpoint allows bulk access to accounts.</p><p>optional pagination parameters for filter with accounts</p><p>Possible custom url parameters for pagination:</p><ul><li>limit=NUMBER ==&gt; default value: 50</li><li>offset=NUMBER ==&gt; default value: 0</li></ul><p>eg1:?limit=100&amp;offset=0</p><ul><li>sort_direction=ASC/DESC ==&gt; default value: DESC.</li></ul><p>eg2:?limit=100&amp;offset=0&amp;sort_direction=ASC</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_fast_firehose_accounts_at_one_bank_with_http_info(bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str bank_id: The bank id (required)
        :return: FastFirehoseAccountsJsonV400
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bank_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fast_firehose_accounts_at_one_bank" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bank_id' is set
        if self.api_client.client_side_validation and ('bank_id' not in params or
                                                       params['bank_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `bank_id` when calling `get_fast_firehose_accounts_at_one_bank`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'bank_id' in params:
            path_params['BANK_ID'] = params['bank_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['directLogin', 'gatewayLogin']  # noqa: E501

        return self.api_client.call_api(
            '/obp/v5.0.0/management/banks/{BANK_ID}/fast-firehose/accounts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FastFirehoseAccountsJsonV400',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_firehose_accounts_at_one_bank(self, view_id, bank_id, **kwargs):  # noqa: E501
        """Get Firehose Accounts at Bank  # noqa: E501

        <p>Get Accounts which have a firehose view assigned to them.</p><p>This endpoint allows bulk access to accounts.</p><p>Requires the CanUseFirehoseAtAnyBank Role</p><p>To be shown on the list, each Account must have a firehose View linked to it.</p><p>A firehose view has is_firehose = true</p><p>For VIEW_ID try 'owner'</p><p>optional request parameters for filter with attributes<br />URL params example:<br />/banks/some-bank-id/firehose/accounts/views/owner?manager=John&amp;count=8</p><p>to invalid Browser cache, add timestamp query parameter as follow, the parameter name must be <code>_timestamp_</code><br />URL params example:<br /><code>/banks/some-bank-id/firehose/accounts/views/owner?manager=John&amp;count=8&amp;_timestamp_=1596762180358</code></p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_firehose_accounts_at_one_bank(view_id, bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str view_id: The view id (required)
        :param str bank_id: The bank id (required)
        :return: ModeratedFirehoseAccountsJsonV400
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_firehose_accounts_at_one_bank_with_http_info(view_id, bank_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_firehose_accounts_at_one_bank_with_http_info(view_id, bank_id, **kwargs)  # noqa: E501
            return data

    def get_firehose_accounts_at_one_bank_with_http_info(self, view_id, bank_id, **kwargs):  # noqa: E501
        """Get Firehose Accounts at Bank  # noqa: E501

        <p>Get Accounts which have a firehose view assigned to them.</p><p>This endpoint allows bulk access to accounts.</p><p>Requires the CanUseFirehoseAtAnyBank Role</p><p>To be shown on the list, each Account must have a firehose View linked to it.</p><p>A firehose view has is_firehose = true</p><p>For VIEW_ID try 'owner'</p><p>optional request parameters for filter with attributes<br />URL params example:<br />/banks/some-bank-id/firehose/accounts/views/owner?manager=John&amp;count=8</p><p>to invalid Browser cache, add timestamp query parameter as follow, the parameter name must be <code>_timestamp_</code><br />URL params example:<br /><code>/banks/some-bank-id/firehose/accounts/views/owner?manager=John&amp;count=8&amp;_timestamp_=1596762180358</code></p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_firehose_accounts_at_one_bank_with_http_info(view_id, bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str view_id: The view id (required)
        :param str bank_id: The bank id (required)
        :return: ModeratedFirehoseAccountsJsonV400
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['view_id', 'bank_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_firehose_accounts_at_one_bank" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'view_id' is set
        if self.api_client.client_side_validation and ('view_id' not in params or
                                                       params['view_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `view_id` when calling `get_firehose_accounts_at_one_bank`")  # noqa: E501
        # verify the required parameter 'bank_id' is set
        if self.api_client.client_side_validation and ('bank_id' not in params or
                                                       params['bank_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `bank_id` when calling `get_firehose_accounts_at_one_bank`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'view_id' in params:
            path_params['VIEW_ID'] = params['view_id']  # noqa: E501
        if 'bank_id' in params:
            path_params['BANK_ID'] = params['bank_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['directLogin', 'gatewayLogin']  # noqa: E501

        return self.api_client.call_api(
            '/obp/v5.0.0/banks/{BANK_ID}/firehose/accounts/views/{VIEW_ID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ModeratedFirehoseAccountsJsonV400',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_firehose_transactions_for_bank_account(self, body, view_id, account_id, bank_id, **kwargs):  # noqa: E501
        """Get Firehose Transactions for Account  # noqa: E501

        <p>Get Transactions for an Account that has a firehose View.</p><p>Allows bulk access to an account's transactions.<br />User must have the CanUseFirehoseAtAnyBank Role</p><p>To find ACCOUNT_IDs, use the getFirehoseAccountsAtOneBank call.</p><p>For VIEW_ID try 'owner'</p><p>Possible custom url parameters for pagination:</p><ul><li>limit=NUMBER ==&gt; default value: 50</li><li>offset=NUMBER ==&gt; default value: 0</li></ul><p>eg1:?limit=100&amp;offset=0</p><ul><li>sort_direction=ASC/DESC ==&gt; default value: DESC.</li></ul><p>eg2:?limit=100&amp;offset=0&amp;sort_direction=ASC</p><ul><li>from_date=DATE =&gt; example value: 1970-01-01T00:00:00.000Z. NOTE! The default value is one year ago (1970-01-01T00:00:00.000Z).</li><li>to_date=DATE =&gt; example value: 2022-10-07T16:42:23.299Z. NOTE! The default value is now (2022-10-07T16:42:23.299Z).</li></ul><p>Date format parameter: yyyy-MM-dd'T'HH:mm:ss.SSS'Z'(1100-01-01T01:01:01.000Z) ==&gt; time zone is UTC.</p><p>eg3:?sort_direction=ASC&amp;limit=100&amp;offset=0&amp;from_date=1100-01-01T01:01:01.000Z&amp;to_date=1100-01-01T01:01:01.000Z</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_firehose_transactions_for_bank_account(body, view_id, account_id, bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EmptyClassJson body: EmptyClassJson object that needs to be added. (required)
        :param str view_id: The view id (required)
        :param str account_id: The account id (required)
        :param str bank_id: The bank id (required)
        :return: TransactionsJsonV300
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_firehose_transactions_for_bank_account_with_http_info(body, view_id, account_id, bank_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_firehose_transactions_for_bank_account_with_http_info(body, view_id, account_id, bank_id, **kwargs)  # noqa: E501
            return data

    def get_firehose_transactions_for_bank_account_with_http_info(self, body, view_id, account_id, bank_id, **kwargs):  # noqa: E501
        """Get Firehose Transactions for Account  # noqa: E501

        <p>Get Transactions for an Account that has a firehose View.</p><p>Allows bulk access to an account's transactions.<br />User must have the CanUseFirehoseAtAnyBank Role</p><p>To find ACCOUNT_IDs, use the getFirehoseAccountsAtOneBank call.</p><p>For VIEW_ID try 'owner'</p><p>Possible custom url parameters for pagination:</p><ul><li>limit=NUMBER ==&gt; default value: 50</li><li>offset=NUMBER ==&gt; default value: 0</li></ul><p>eg1:?limit=100&amp;offset=0</p><ul><li>sort_direction=ASC/DESC ==&gt; default value: DESC.</li></ul><p>eg2:?limit=100&amp;offset=0&amp;sort_direction=ASC</p><ul><li>from_date=DATE =&gt; example value: 1970-01-01T00:00:00.000Z. NOTE! The default value is one year ago (1970-01-01T00:00:00.000Z).</li><li>to_date=DATE =&gt; example value: 2022-10-07T16:42:23.299Z. NOTE! The default value is now (2022-10-07T16:42:23.299Z).</li></ul><p>Date format parameter: yyyy-MM-dd'T'HH:mm:ss.SSS'Z'(1100-01-01T01:01:01.000Z) ==&gt; time zone is UTC.</p><p>eg3:?sort_direction=ASC&amp;limit=100&amp;offset=0&amp;from_date=1100-01-01T01:01:01.000Z&amp;to_date=1100-01-01T01:01:01.000Z</p><p>Authentication is Mandatory</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_firehose_transactions_for_bank_account_with_http_info(body, view_id, account_id, bank_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EmptyClassJson body: EmptyClassJson object that needs to be added. (required)
        :param str view_id: The view id (required)
        :param str account_id: The account id (required)
        :param str bank_id: The bank id (required)
        :return: TransactionsJsonV300
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'view_id', 'account_id', 'bank_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_firehose_transactions_for_bank_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `get_firehose_transactions_for_bank_account`")  # noqa: E501
        # verify the required parameter 'view_id' is set
        if self.api_client.client_side_validation and ('view_id' not in params or
                                                       params['view_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `view_id` when calling `get_firehose_transactions_for_bank_account`")  # noqa: E501
        # verify the required parameter 'account_id' is set
        if self.api_client.client_side_validation and ('account_id' not in params or
                                                       params['account_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `account_id` when calling `get_firehose_transactions_for_bank_account`")  # noqa: E501
        # verify the required parameter 'bank_id' is set
        if self.api_client.client_side_validation and ('bank_id' not in params or
                                                       params['bank_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `bank_id` when calling `get_firehose_transactions_for_bank_account`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'view_id' in params:
            path_params['VIEW_ID'] = params['view_id']  # noqa: E501
        if 'account_id' in params:
            path_params['ACCOUNT_ID'] = params['account_id']  # noqa: E501
        if 'bank_id' in params:
            path_params['BANK_ID'] = params['bank_id']  # noqa: E501

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
            '/obp/v5.0.0/banks/{BANK_ID}/firehose/accounts/{ACCOUNT_ID}/views/{VIEW_ID}/transactions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TransactionsJsonV300',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
