from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.get_global_messages_scopes_item import GetGlobalMessagesScopesItem
from ...models.message import Message
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    group: Union[Unset, None, str] = UNSET,
    language: Union[Unset, None, str] = UNSET,
    read: Union[Unset, None, bool] = UNSET,
    scopes: Union[Unset, None, List[GetGlobalMessagesScopesItem]] = UNSET,
    output_fields: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/messages".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["group"] = group

    params["language"] = language

    params["read"] = read

    json_scopes: Union[Unset, None, List[str]] = UNSET
    if not isinstance(scopes, Unset):
        if scopes is None:
            json_scopes = None
        else:
            json_scopes = []
            for scopes_item_data in scopes:
                scopes_item = scopes_item_data.value

                json_scopes.append(scopes_item)

    params["scopes"] = json_scopes

    params["outputFields"] = output_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[List["Message"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_message_array_item_data in _response_200:
            componentsschemas_message_array_item = Message.from_dict(componentsschemas_message_array_item_data)

            response_200.append(componentsschemas_message_array_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[List["Message"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    group: Union[Unset, None, str] = UNSET,
    language: Union[Unset, None, str] = UNSET,
    read: Union[Unset, None, bool] = UNSET,
    scopes: Union[Unset, None, List[GetGlobalMessagesScopesItem]] = UNSET,
    output_fields: Union[Unset, None, str] = UNSET,
) -> Response[List["Message"]]:
    """Get messages of current user

    Args:
        group (Union[Unset, None, str]):
        language (Union[Unset, None, str]):
        read (Union[Unset, None, bool]):
        scopes (Union[Unset, None, List[GetGlobalMessagesScopesItem]]):
        output_fields (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['Message']]
    """

    kwargs = _get_kwargs(
        client=client,
        group=group,
        language=language,
        read=read,
        scopes=scopes,
        output_fields=output_fields,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    group: Union[Unset, None, str] = UNSET,
    language: Union[Unset, None, str] = UNSET,
    read: Union[Unset, None, bool] = UNSET,
    scopes: Union[Unset, None, List[GetGlobalMessagesScopesItem]] = UNSET,
    output_fields: Union[Unset, None, str] = UNSET,
) -> Optional[List["Message"]]:
    """Get messages of current user

    Args:
        group (Union[Unset, None, str]):
        language (Union[Unset, None, str]):
        read (Union[Unset, None, bool]):
        scopes (Union[Unset, None, List[GetGlobalMessagesScopesItem]]):
        output_fields (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['Message']]
    """

    return sync_detailed(
        client=client,
        group=group,
        language=language,
        read=read,
        scopes=scopes,
        output_fields=output_fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    group: Union[Unset, None, str] = UNSET,
    language: Union[Unset, None, str] = UNSET,
    read: Union[Unset, None, bool] = UNSET,
    scopes: Union[Unset, None, List[GetGlobalMessagesScopesItem]] = UNSET,
    output_fields: Union[Unset, None, str] = UNSET,
) -> Response[List["Message"]]:
    """Get messages of current user

    Args:
        group (Union[Unset, None, str]):
        language (Union[Unset, None, str]):
        read (Union[Unset, None, bool]):
        scopes (Union[Unset, None, List[GetGlobalMessagesScopesItem]]):
        output_fields (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['Message']]
    """

    kwargs = _get_kwargs(
        client=client,
        group=group,
        language=language,
        read=read,
        scopes=scopes,
        output_fields=output_fields,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    group: Union[Unset, None, str] = UNSET,
    language: Union[Unset, None, str] = UNSET,
    read: Union[Unset, None, bool] = UNSET,
    scopes: Union[Unset, None, List[GetGlobalMessagesScopesItem]] = UNSET,
    output_fields: Union[Unset, None, str] = UNSET,
) -> Optional[List["Message"]]:
    """Get messages of current user

    Args:
        group (Union[Unset, None, str]):
        language (Union[Unset, None, str]):
        read (Union[Unset, None, bool]):
        scopes (Union[Unset, None, List[GetGlobalMessagesScopesItem]]):
        output_fields (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['Message']]
    """

    return (
        await asyncio_detailed(
            client=client,
            group=group,
            language=language,
            read=read,
            scopes=scopes,
            output_fields=output_fields,
        )
    ).parsed
