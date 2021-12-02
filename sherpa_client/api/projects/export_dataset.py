from typing import Any, Dict, List, Optional

import httpx

from ...client import Client
from ...models.segment import Segment
from ...types import Response


def _get_kwargs(
    project_name: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/projects/{projectName}/dataset".format(client.base_url, projectName=project_name)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[Segment]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_segment_array_item_data in _response_200:
            componentsschemas_segment_array_item = Segment.from_dict(componentsschemas_segment_array_item_data)

            response_200.append(componentsschemas_segment_array_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[Segment]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    project_name: str,
    *,
    client: Client,
) -> Response[List[Segment]]:
    kwargs = _get_kwargs(
        project_name=project_name,
        client=client,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    project_name: str,
    *,
    client: Client,
) -> Optional[List[Segment]]:
    """ """

    return sync_detailed(
        project_name=project_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_name: str,
    *,
    client: Client,
) -> Response[List[Segment]]:
    kwargs = _get_kwargs(
        project_name=project_name,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    project_name: str,
    *,
    client: Client,
) -> Optional[List[Segment]]:
    """ """

    return (
        await asyncio_detailed(
            project_name=project_name,
            client=client,
        )
    ).parsed
