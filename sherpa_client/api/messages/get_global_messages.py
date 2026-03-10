from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_global_messages_output_format import GetGlobalMessagesOutputFormat
from ...models.get_global_messages_scope_item import GetGlobalMessagesScopeItem
from ...models.global_message import GlobalMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    language: Union[Unset, str] = UNSET,
    fallback_languages: Union[Unset, str] = UNSET,
    read: Union[Unset, bool] = UNSET,
    group: Union[Unset, list[str]] = UNSET,
    scope: Union[Unset, list[GetGlobalMessagesScopeItem]] = UNSET,
    output_format: Union[Unset, GetGlobalMessagesOutputFormat] = UNSET,
    run_templates: Union[Unset, bool] = False,
    output_fields: Union[Unset, str] = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["language"] = language

    params["fallbackLanguages"] = fallback_languages

    params["read"] = read

    json_group: Union[Unset, list[str]] = UNSET
    if not isinstance(group, Unset):
        json_group = group

    params["group"] = json_group

    json_scope: Union[Unset, list[str]] = UNSET
    if not isinstance(scope, Unset):
        json_scope = []
        for scope_item_data in scope:
            scope_item = scope_item_data.value
            json_scope.append(scope_item)

    params["scope"] = json_scope

    json_output_format: Union[Unset, str] = UNSET
    if not isinstance(output_format, Unset):
        json_output_format = output_format.value

    params["outputFormat"] = json_output_format

    params["runTemplates"] = run_templates

    params["outputFields"] = output_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/messages",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["GlobalMessage"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_global_message_array_item_data in _response_200:
            componentsschemas_global_message_array_item = GlobalMessage.from_dict(
                componentsschemas_global_message_array_item_data
            )

            response_200.append(componentsschemas_global_message_array_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["GlobalMessage"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    language: Union[Unset, str] = UNSET,
    fallback_languages: Union[Unset, str] = UNSET,
    read: Union[Unset, bool] = UNSET,
    group: Union[Unset, list[str]] = UNSET,
    scope: Union[Unset, list[GetGlobalMessagesScopeItem]] = UNSET,
    output_format: Union[Unset, GetGlobalMessagesOutputFormat] = UNSET,
    run_templates: Union[Unset, bool] = False,
    output_fields: Union[Unset, str] = UNSET,
) -> Response[list["GlobalMessage"]]:
    """Get messages of current user

    Args:
        language (Union[Unset, str]):
        fallback_languages (Union[Unset, str]):
        read (Union[Unset, bool]):
        group (Union[Unset, list[str]]):
        scope (Union[Unset, list[GetGlobalMessagesScopeItem]]):
        output_format (Union[Unset, GetGlobalMessagesOutputFormat]):
        run_templates (Union[Unset, bool]):  Default: False.
        output_fields (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['GlobalMessage']]
    """

    kwargs = _get_kwargs(
        language=language,
        fallback_languages=fallback_languages,
        read=read,
        group=group,
        scope=scope,
        output_format=output_format,
        run_templates=run_templates,
        output_fields=output_fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    language: Union[Unset, str] = UNSET,
    fallback_languages: Union[Unset, str] = UNSET,
    read: Union[Unset, bool] = UNSET,
    group: Union[Unset, list[str]] = UNSET,
    scope: Union[Unset, list[GetGlobalMessagesScopeItem]] = UNSET,
    output_format: Union[Unset, GetGlobalMessagesOutputFormat] = UNSET,
    run_templates: Union[Unset, bool] = False,
    output_fields: Union[Unset, str] = UNSET,
) -> Optional[list["GlobalMessage"]]:
    """Get messages of current user

    Args:
        language (Union[Unset, str]):
        fallback_languages (Union[Unset, str]):
        read (Union[Unset, bool]):
        group (Union[Unset, list[str]]):
        scope (Union[Unset, list[GetGlobalMessagesScopeItem]]):
        output_format (Union[Unset, GetGlobalMessagesOutputFormat]):
        run_templates (Union[Unset, bool]):  Default: False.
        output_fields (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['GlobalMessage']
    """

    return sync_detailed(
        client=client,
        language=language,
        fallback_languages=fallback_languages,
        read=read,
        group=group,
        scope=scope,
        output_format=output_format,
        run_templates=run_templates,
        output_fields=output_fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    language: Union[Unset, str] = UNSET,
    fallback_languages: Union[Unset, str] = UNSET,
    read: Union[Unset, bool] = UNSET,
    group: Union[Unset, list[str]] = UNSET,
    scope: Union[Unset, list[GetGlobalMessagesScopeItem]] = UNSET,
    output_format: Union[Unset, GetGlobalMessagesOutputFormat] = UNSET,
    run_templates: Union[Unset, bool] = False,
    output_fields: Union[Unset, str] = UNSET,
) -> Response[list["GlobalMessage"]]:
    """Get messages of current user

    Args:
        language (Union[Unset, str]):
        fallback_languages (Union[Unset, str]):
        read (Union[Unset, bool]):
        group (Union[Unset, list[str]]):
        scope (Union[Unset, list[GetGlobalMessagesScopeItem]]):
        output_format (Union[Unset, GetGlobalMessagesOutputFormat]):
        run_templates (Union[Unset, bool]):  Default: False.
        output_fields (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['GlobalMessage']]
    """

    kwargs = _get_kwargs(
        language=language,
        fallback_languages=fallback_languages,
        read=read,
        group=group,
        scope=scope,
        output_format=output_format,
        run_templates=run_templates,
        output_fields=output_fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    language: Union[Unset, str] = UNSET,
    fallback_languages: Union[Unset, str] = UNSET,
    read: Union[Unset, bool] = UNSET,
    group: Union[Unset, list[str]] = UNSET,
    scope: Union[Unset, list[GetGlobalMessagesScopeItem]] = UNSET,
    output_format: Union[Unset, GetGlobalMessagesOutputFormat] = UNSET,
    run_templates: Union[Unset, bool] = False,
    output_fields: Union[Unset, str] = UNSET,
) -> Optional[list["GlobalMessage"]]:
    """Get messages of current user

    Args:
        language (Union[Unset, str]):
        fallback_languages (Union[Unset, str]):
        read (Union[Unset, bool]):
        group (Union[Unset, list[str]]):
        scope (Union[Unset, list[GetGlobalMessagesScopeItem]]):
        output_format (Union[Unset, GetGlobalMessagesOutputFormat]):
        run_templates (Union[Unset, bool]):  Default: False.
        output_fields (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['GlobalMessage']
    """

    return (
        await asyncio_detailed(
            client=client,
            language=language,
            fallback_languages=fallback_languages,
            read=read,
            group=group,
            scope=scope,
            output_format=output_format,
            run_templates=run_templates,
            output_fields=output_fields,
        )
    ).parsed
