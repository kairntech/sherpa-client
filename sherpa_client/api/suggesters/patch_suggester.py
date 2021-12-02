from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.suggester import Suggester
from ...types import Response


def _get_kwargs(
    project_name: str,
    name: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/projects/{projectName}/suggesters/{name}".format(client.base_url, projectName=project_name, name=name)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Suggester]]:
    if response.status_code == 200:
        response_200 = Suggester.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = None

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Suggester]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    project_name: str,
    name: str,
    *,
    client: Client,
) -> Response[Union[Any, Suggester]]:
    kwargs = _get_kwargs(
        project_name=project_name,
        name=name,
        client=client,
    )

    response = httpx.patch(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    project_name: str,
    name: str,
    *,
    client: Client,
) -> Optional[Union[Any, Suggester]]:
    """ """

    return sync_detailed(
        project_name=project_name,
        name=name,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_name: str,
    name: str,
    *,
    client: Client,
) -> Response[Union[Any, Suggester]]:
    kwargs = _get_kwargs(
        project_name=project_name,
        name=name,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.patch(**kwargs)

    return _build_response(response=response)


async def asyncio(
    project_name: str,
    name: str,
    *,
    client: Client,
) -> Optional[Union[Any, Suggester]]:
    """ """

    return (
        await asyncio_detailed(
            project_name=project_name,
            name=name,
            client=client,
        )
    ).parsed
