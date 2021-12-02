from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.engine_name import EngineName
from ...models.new_named_annotation_plan import NewNamedAnnotationPlan
from ...types import Response


def _get_kwargs(
    project_name: str,
    *,
    client: Client,
    json_body: NewNamedAnnotationPlan,
) -> Dict[str, Any]:
    url = "{}/projects/{projectName}/plans".format(client.base_url, projectName=project_name)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[EngineName]:
    if response.status_code == 200:
        response_200 = EngineName.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[EngineName]:
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
    json_body: NewNamedAnnotationPlan,
) -> Response[EngineName]:
    kwargs = _get_kwargs(
        project_name=project_name,
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    project_name: str,
    *,
    client: Client,
    json_body: NewNamedAnnotationPlan,
) -> Optional[EngineName]:
    """ """

    return sync_detailed(
        project_name=project_name,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    project_name: str,
    *,
    client: Client,
    json_body: NewNamedAnnotationPlan,
) -> Response[EngineName]:
    kwargs = _get_kwargs(
        project_name=project_name,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    project_name: str,
    *,
    client: Client,
    json_body: NewNamedAnnotationPlan,
) -> Optional[EngineName]:
    """ """

    return (
        await asyncio_detailed(
            project_name=project_name,
            client=client,
            json_body=json_body,
        )
    ).parsed
