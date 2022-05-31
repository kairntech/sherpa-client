from typing import Any, Dict, List, Optional

import httpx

from ...client import Client
from ...models.metadata_definition import MetadataDefinition
from ...types import Response


def _get_kwargs(
    project_name: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/projects/{projectName}/metadata".format(client.base_url, projectName=project_name)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[MetadataDefinition]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_metadata_definition_array_item_data in _response_200:
            componentsschemas_metadata_definition_array_item = MetadataDefinition.from_dict(
                componentsschemas_metadata_definition_array_item_data
            )

            response_200.append(componentsschemas_metadata_definition_array_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[MetadataDefinition]]:
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
) -> Response[List[MetadataDefinition]]:
    """get the list of known metadata in this project

    Args:
        project_name (str):

    Returns:
        Response[List[MetadataDefinition]]
    """

    kwargs = _get_kwargs(
        project_name=project_name,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    project_name: str,
    *,
    client: Client,
) -> Optional[List[MetadataDefinition]]:
    """get the list of known metadata in this project

    Args:
        project_name (str):

    Returns:
        Response[List[MetadataDefinition]]
    """

    return sync_detailed(
        project_name=project_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_name: str,
    *,
    client: Client,
) -> Response[List[MetadataDefinition]]:
    """get the list of known metadata in this project

    Args:
        project_name (str):

    Returns:
        Response[List[MetadataDefinition]]
    """

    kwargs = _get_kwargs(
        project_name=project_name,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    project_name: str,
    *,
    client: Client,
) -> Optional[List[MetadataDefinition]]:
    """get the list of known metadata in this project

    Args:
        project_name (str):

    Returns:
        Response[List[MetadataDefinition]]
    """

    return (
        await asyncio_detailed(
            project_name=project_name,
            client=client,
        )
    ).parsed
