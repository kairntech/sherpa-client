from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.facet_configuration import FacetConfiguration
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    enabled_only: Union[Unset, bool] = False,
    nature: Union[Unset, str] = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["enabledOnly"] = enabled_only

    params["nature"] = nature

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/facets",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[list["FacetConfiguration"]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_facet_configuration_array_item_data in _response_200:
            componentsschemas_facet_configuration_array_item = (
                FacetConfiguration.from_dict(
                    componentsschemas_facet_configuration_array_item_data
                )
            )

            response_200.append(componentsschemas_facet_configuration_array_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[list["FacetConfiguration"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    enabled_only: Union[Unset, bool] = False,
    nature: Union[Unset, str] = UNSET,
) -> Response[list["FacetConfiguration"]]:
    """Get all facets configuration

    Args:
        enabled_only (Union[Unset, bool]):  Default: False.
        nature (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['FacetConfiguration']]
    """

    kwargs = _get_kwargs(
        enabled_only=enabled_only,
        nature=nature,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    enabled_only: Union[Unset, bool] = False,
    nature: Union[Unset, str] = UNSET,
) -> Optional[list["FacetConfiguration"]]:
    """Get all facets configuration

    Args:
        enabled_only (Union[Unset, bool]):  Default: False.
        nature (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['FacetConfiguration']
    """

    return sync_detailed(
        client=client,
        enabled_only=enabled_only,
        nature=nature,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    enabled_only: Union[Unset, bool] = False,
    nature: Union[Unset, str] = UNSET,
) -> Response[list["FacetConfiguration"]]:
    """Get all facets configuration

    Args:
        enabled_only (Union[Unset, bool]):  Default: False.
        nature (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['FacetConfiguration']]
    """

    kwargs = _get_kwargs(
        enabled_only=enabled_only,
        nature=nature,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    enabled_only: Union[Unset, bool] = False,
    nature: Union[Unset, str] = UNSET,
) -> Optional[list["FacetConfiguration"]]:
    """Get all facets configuration

    Args:
        enabled_only (Union[Unset, bool]):  Default: False.
        nature (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['FacetConfiguration']
    """

    return (
        await asyncio_detailed(
            client=client,
            enabled_only=enabled_only,
            nature=nature,
        )
    ).parsed
