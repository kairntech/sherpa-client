from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.doc_search_request import DocSearchRequest
from ...models.document_hits import DocumentHits
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_name: str,
    *,
    body: DocSearchRequest,
    html_version: Union[Unset, bool] = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["htmlVersion"] = html_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_name}/documents/_do_search".format(
            project_name=project_name,
        ),
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DocumentHits]:
    if response.status_code == 200:
        response_200 = DocumentHits.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DocumentHits]:
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
    body: DocSearchRequest,
    html_version: Union[Unset, bool] = False,
) -> Response[DocumentHits]:
    """Search for documents

    Args:
        project_name (str):
        html_version (Union[Unset, bool]):  Default: False.
        body (DocSearchRequest): Document search request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DocumentHits]
    """

    kwargs = _get_kwargs(
        project_name=project_name,
        body=body,
        html_version=html_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DocSearchRequest,
    html_version: Union[Unset, bool] = False,
) -> Optional[DocumentHits]:
    """Search for documents

    Args:
        project_name (str):
        html_version (Union[Unset, bool]):  Default: False.
        body (DocSearchRequest): Document search request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DocumentHits
    """

    return sync_detailed(
        project_name=project_name,
        client=client,
        body=body,
        html_version=html_version,
    ).parsed


async def asyncio_detailed(
    project_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DocSearchRequest,
    html_version: Union[Unset, bool] = False,
) -> Response[DocumentHits]:
    """Search for documents

    Args:
        project_name (str):
        html_version (Union[Unset, bool]):  Default: False.
        body (DocSearchRequest): Document search request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DocumentHits]
    """

    kwargs = _get_kwargs(
        project_name=project_name,
        body=body,
        html_version=html_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DocSearchRequest,
    html_version: Union[Unset, bool] = False,
) -> Optional[DocumentHits]:
    """Search for documents

    Args:
        project_name (str):
        html_version (Union[Unset, bool]):  Default: False.
        body (DocSearchRequest): Document search request

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DocumentHits
    """

    return (
        await asyncio_detailed(
            project_name=project_name,
            client=client,
            body=body,
            html_version=html_version,
        )
    ).parsed
