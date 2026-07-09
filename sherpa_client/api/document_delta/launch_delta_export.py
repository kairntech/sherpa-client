from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sherpa_job_bean import SherpaJobBean
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_name: str,
    *,
    output_fields: Union[Unset, str] = UNSET,
    output_fields_modifier: Union[Unset, str] = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["outputFields"] = output_fields

    params["outputFieldsModifier"] = output_fields_modifier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_name}/delta/documents/_export_async".format(
            project_name=project_name,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SherpaJobBean]:
    if response.status_code == 200:
        response_200 = SherpaJobBean.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SherpaJobBean]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    output_fields: Union[Unset, str] = UNSET,
    output_fields_modifier: Union[Unset, str] = UNSET,
) -> Response[SherpaJobBean]:
    """Export modified and deleted documents since the start of the last recording.

    Args:
        project_name (str):
        output_fields (Union[Unset, str]):
        output_fields_modifier (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SherpaJobBean]
    """

    kwargs = _get_kwargs(
        project_name=project_name,
        output_fields=output_fields,
        output_fields_modifier=output_fields_modifier,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    output_fields: Union[Unset, str] = UNSET,
    output_fields_modifier: Union[Unset, str] = UNSET,
) -> Optional[SherpaJobBean]:
    """Export modified and deleted documents since the start of the last recording.

    Args:
        project_name (str):
        output_fields (Union[Unset, str]):
        output_fields_modifier (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SherpaJobBean
    """

    return sync_detailed(
        project_name=project_name,
        client=client,
        output_fields=output_fields,
        output_fields_modifier=output_fields_modifier,
    ).parsed


async def asyncio_detailed(
    project_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    output_fields: Union[Unset, str] = UNSET,
    output_fields_modifier: Union[Unset, str] = UNSET,
) -> Response[SherpaJobBean]:
    """Export modified and deleted documents since the start of the last recording.

    Args:
        project_name (str):
        output_fields (Union[Unset, str]):
        output_fields_modifier (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SherpaJobBean]
    """

    kwargs = _get_kwargs(
        project_name=project_name,
        output_fields=output_fields,
        output_fields_modifier=output_fields_modifier,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    output_fields: Union[Unset, str] = UNSET,
    output_fields_modifier: Union[Unset, str] = UNSET,
) -> Optional[SherpaJobBean]:
    """Export modified and deleted documents since the start of the last recording.

    Args:
        project_name (str):
        output_fields (Union[Unset, str]):
        output_fields_modifier (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SherpaJobBean
    """

    return (
        await asyncio_detailed(
            project_name=project_name,
            client=client,
            output_fields=output_fields,
            output_fields_modifier=output_fields_modifier,
        )
    ).parsed
