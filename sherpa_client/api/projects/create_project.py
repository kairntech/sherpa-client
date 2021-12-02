from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.project_config_creation import ProjectConfigCreation
from ...models.project_status import ProjectStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: ProjectConfigCreation,
    group_name: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/projects".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "groupName": group_name,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[ProjectStatus]:
    if response.status_code == 200:
        response_200 = ProjectStatus.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ProjectStatus]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: ProjectConfigCreation,
    group_name: Union[Unset, None, str] = UNSET,
) -> Response[ProjectStatus]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        group_name=group_name,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: ProjectConfigCreation,
    group_name: Union[Unset, None, str] = UNSET,
) -> Optional[ProjectStatus]:
    """ """

    return sync_detailed(
        client=client,
        json_body=json_body,
        group_name=group_name,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: ProjectConfigCreation,
    group_name: Union[Unset, None, str] = UNSET,
) -> Response[ProjectStatus]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        group_name=group_name,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: ProjectConfigCreation,
    group_name: Union[Unset, None, str] = UNSET,
) -> Optional[ProjectStatus]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            group_name=group_name,
        )
    ).parsed
