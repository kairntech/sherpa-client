from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.users_response import UsersResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    group_name: Union[Unset, None, str] = UNSET,
    admin_data: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/users".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["groupName"] = group_name

    params["adminData"] = admin_data

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[UsersResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = UsersResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[UsersResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    group_name: Union[Unset, None, str] = UNSET,
    admin_data: Union[Unset, None, bool] = False,
) -> Response[UsersResponse]:
    """Get users

    Args:
        group_name (Union[Unset, None, str]):
        admin_data (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsersResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        group_name=group_name,
        admin_data=admin_data,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    group_name: Union[Unset, None, str] = UNSET,
    admin_data: Union[Unset, None, bool] = False,
) -> Optional[UsersResponse]:
    """Get users

    Args:
        group_name (Union[Unset, None, str]):
        admin_data (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsersResponse]
    """

    return sync_detailed(
        client=client,
        group_name=group_name,
        admin_data=admin_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    group_name: Union[Unset, None, str] = UNSET,
    admin_data: Union[Unset, None, bool] = False,
) -> Response[UsersResponse]:
    """Get users

    Args:
        group_name (Union[Unset, None, str]):
        admin_data (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsersResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        group_name=group_name,
        admin_data=admin_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    group_name: Union[Unset, None, str] = UNSET,
    admin_data: Union[Unset, None, bool] = False,
) -> Optional[UsersResponse]:
    """Get users

    Args:
        group_name (Union[Unset, None, str]):
        admin_data (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UsersResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            group_name=group_name,
            admin_data=admin_data,
        )
    ).parsed
