from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.ack import Ack
from ...models.update_theme_form import UpdateThemeForm
from ...types import Response


def _get_kwargs(
    theme_id: str,
    *,
    client: Client,
    multipart_data: UpdateThemeForm,
) -> Dict[str, Any]:
    url = "{}/themes/{themeId}/_update".format(client.base_url, themeId=theme_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Ack, Any]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Ack.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Ack, Any]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    theme_id: str,
    *,
    client: Client,
    multipart_data: UpdateThemeForm,
) -> Response[Union[Ack, Any]]:
    """Update a UI theme

    Args:
        theme_id (str):
        multipart_data (UpdateThemeForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Ack, Any]]
    """

    kwargs = _get_kwargs(
        theme_id=theme_id,
        client=client,
        multipart_data=multipart_data,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    theme_id: str,
    *,
    client: Client,
    multipart_data: UpdateThemeForm,
) -> Optional[Union[Ack, Any]]:
    """Update a UI theme

    Args:
        theme_id (str):
        multipart_data (UpdateThemeForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Ack, Any]]
    """

    return sync_detailed(
        theme_id=theme_id,
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    theme_id: str,
    *,
    client: Client,
    multipart_data: UpdateThemeForm,
) -> Response[Union[Ack, Any]]:
    """Update a UI theme

    Args:
        theme_id (str):
        multipart_data (UpdateThemeForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Ack, Any]]
    """

    kwargs = _get_kwargs(
        theme_id=theme_id,
        client=client,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    theme_id: str,
    *,
    client: Client,
    multipart_data: UpdateThemeForm,
) -> Optional[Union[Ack, Any]]:
    """Update a UI theme

    Args:
        theme_id (str):
        multipart_data (UpdateThemeForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Ack, Any]]
    """

    return (
        await asyncio_detailed(
            theme_id=theme_id,
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
