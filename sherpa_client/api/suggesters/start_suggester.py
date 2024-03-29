from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.ack import Ack
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_name: str,
    name: str,
    *,
    client: Client,
    force_training: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/projects/{projectName}/suggesters/{name}/_start".format(
        client.base_url, projectName=project_name, name=name
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["forceTraining"] = force_training

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
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
    project_name: str,
    name: str,
    *,
    client: Client,
    force_training: Union[Unset, None, bool] = False,
) -> Response[Union[Ack, Any]]:
    """Start a suggester

    Args:
        project_name (str):
        name (str):
        force_training (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Ack, Any]]
    """

    kwargs = _get_kwargs(
        project_name=project_name,
        name=name,
        client=client,
        force_training=force_training,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_name: str,
    name: str,
    *,
    client: Client,
    force_training: Union[Unset, None, bool] = False,
) -> Optional[Union[Ack, Any]]:
    """Start a suggester

    Args:
        project_name (str):
        name (str):
        force_training (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Ack, Any]]
    """

    return sync_detailed(
        project_name=project_name,
        name=name,
        client=client,
        force_training=force_training,
    ).parsed


async def asyncio_detailed(
    project_name: str,
    name: str,
    *,
    client: Client,
    force_training: Union[Unset, None, bool] = False,
) -> Response[Union[Ack, Any]]:
    """Start a suggester

    Args:
        project_name (str):
        name (str):
        force_training (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Ack, Any]]
    """

    kwargs = _get_kwargs(
        project_name=project_name,
        name=name,
        client=client,
        force_training=force_training,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_name: str,
    name: str,
    *,
    client: Client,
    force_training: Union[Unset, None, bool] = False,
) -> Optional[Union[Ack, Any]]:
    """Start a suggester

    Args:
        project_name (str):
        name (str):
        force_training (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Ack, Any]]
    """

    return (
        await asyncio_detailed(
            project_name=project_name,
            name=name,
            client=client,
            force_training=force_training,
        )
    ).parsed
