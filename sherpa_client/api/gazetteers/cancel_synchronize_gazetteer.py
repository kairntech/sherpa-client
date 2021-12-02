from typing import Any, Dict

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    project_name: str,
    name: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/projects/{projectName}/gazetteers/{name}/_cancel_synchronize".format(
        client.base_url, projectName=project_name, name=name
    )

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    project_name: str,
    name: str,
    *,
    client: Client,
) -> Response[Any]:
    kwargs = _get_kwargs(
        project_name=project_name,
        name=name,
        client=client,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    project_name: str,
    name: str,
    *,
    client: Client,
) -> Response[Any]:
    kwargs = _get_kwargs(
        project_name=project_name,
        name=name,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)
