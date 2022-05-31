from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.ack import Ack
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    project_name: str,
) -> Dict[str, Any]:
    url = "{}/projects/_undeploy".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["projectName"] = project_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Ack, Any]]:
    if response.status_code == 200:
        response_200 = Ack.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Ack, Any]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    project_name: str,
) -> Response[Union[Ack, Any]]:
    """undeploy a running project

    Args:
        project_name (str):

    Returns:
        Response[Union[Ack, Any]]
    """

    kwargs = _get_kwargs(
        client=client,
        project_name=project_name,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    project_name: str,
) -> Optional[Union[Ack, Any]]:
    """undeploy a running project

    Args:
        project_name (str):

    Returns:
        Response[Union[Ack, Any]]
    """

    return sync_detailed(
        client=client,
        project_name=project_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    project_name: str,
) -> Response[Union[Ack, Any]]:
    """undeploy a running project

    Args:
        project_name (str):

    Returns:
        Response[Union[Ack, Any]]
    """

    kwargs = _get_kwargs(
        client=client,
        project_name=project_name,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    project_name: str,
) -> Optional[Union[Ack, Any]]:
    """undeploy a running project

    Args:
        project_name (str):

    Returns:
        Response[Union[Ack, Any]]
    """

    return (
        await asyncio_detailed(
            client=client,
            project_name=project_name,
        )
    ).parsed
