from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.annotate_binary_with_project_multipart_data import AnnotateBinaryWithProjectMultipartData
from ...models.annotated_document import AnnotatedDocument
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_name: str,
    *,
    client: Client,
    multipart_data: AnnotateBinaryWithProjectMultipartData,
    inline_labels: Union[Unset, None, bool] = True,
    inline_label_ids: Union[Unset, None, bool] = True,
    inline_text: Union[Unset, None, bool] = True,
    debug: Union[Unset, None, bool] = False,
    parallelize: Union[Unset, None, bool] = False,
    error_policy: Union[Unset, None, str] = UNSET,
    output_fields: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/annotate/projects/{projectName}/_annotate_binary".format(client.base_url, projectName=project_name)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["inlineLabels"] = inline_labels

    params["inlineLabelIds"] = inline_label_ids

    params["inlineText"] = inline_text

    params["debug"] = debug

    params["parallelize"] = parallelize

    params["errorPolicy"] = error_policy

    params["outputFields"] = output_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[List["AnnotatedDocument"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_annotated_document_array_item_data in _response_200:
            componentsschemas_annotated_document_array_item = AnnotatedDocument.from_dict(
                componentsschemas_annotated_document_array_item_data
            )

            response_200.append(componentsschemas_annotated_document_array_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[List["AnnotatedDocument"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_name: str,
    *,
    client: Client,
    multipart_data: AnnotateBinaryWithProjectMultipartData,
    inline_labels: Union[Unset, None, bool] = True,
    inline_label_ids: Union[Unset, None, bool] = True,
    inline_text: Union[Unset, None, bool] = True,
    debug: Union[Unset, None, bool] = False,
    parallelize: Union[Unset, None, bool] = False,
    error_policy: Union[Unset, None, str] = UNSET,
    output_fields: Union[Unset, None, str] = UNSET,
) -> Response[List["AnnotatedDocument"]]:
    """annotate a binary document with the default annotator of the project

    Args:
        project_name (str):
        inline_labels (Union[Unset, None, bool]):  Default: True.
        inline_label_ids (Union[Unset, None, bool]):  Default: True.
        inline_text (Union[Unset, None, bool]):  Default: True.
        debug (Union[Unset, None, bool]):
        parallelize (Union[Unset, None, bool]):
        error_policy (Union[Unset, None, str]):
        output_fields (Union[Unset, None, str]):
        multipart_data (AnnotateBinaryWithProjectMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['AnnotatedDocument']]
    """

    kwargs = _get_kwargs(
        project_name=project_name,
        client=client,
        multipart_data=multipart_data,
        inline_labels=inline_labels,
        inline_label_ids=inline_label_ids,
        inline_text=inline_text,
        debug=debug,
        parallelize=parallelize,
        error_policy=error_policy,
        output_fields=output_fields,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_name: str,
    *,
    client: Client,
    multipart_data: AnnotateBinaryWithProjectMultipartData,
    inline_labels: Union[Unset, None, bool] = True,
    inline_label_ids: Union[Unset, None, bool] = True,
    inline_text: Union[Unset, None, bool] = True,
    debug: Union[Unset, None, bool] = False,
    parallelize: Union[Unset, None, bool] = False,
    error_policy: Union[Unset, None, str] = UNSET,
    output_fields: Union[Unset, None, str] = UNSET,
) -> Optional[List["AnnotatedDocument"]]:
    """annotate a binary document with the default annotator of the project

    Args:
        project_name (str):
        inline_labels (Union[Unset, None, bool]):  Default: True.
        inline_label_ids (Union[Unset, None, bool]):  Default: True.
        inline_text (Union[Unset, None, bool]):  Default: True.
        debug (Union[Unset, None, bool]):
        parallelize (Union[Unset, None, bool]):
        error_policy (Union[Unset, None, str]):
        output_fields (Union[Unset, None, str]):
        multipart_data (AnnotateBinaryWithProjectMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['AnnotatedDocument']]
    """

    return sync_detailed(
        project_name=project_name,
        client=client,
        multipart_data=multipart_data,
        inline_labels=inline_labels,
        inline_label_ids=inline_label_ids,
        inline_text=inline_text,
        debug=debug,
        parallelize=parallelize,
        error_policy=error_policy,
        output_fields=output_fields,
    ).parsed


async def asyncio_detailed(
    project_name: str,
    *,
    client: Client,
    multipart_data: AnnotateBinaryWithProjectMultipartData,
    inline_labels: Union[Unset, None, bool] = True,
    inline_label_ids: Union[Unset, None, bool] = True,
    inline_text: Union[Unset, None, bool] = True,
    debug: Union[Unset, None, bool] = False,
    parallelize: Union[Unset, None, bool] = False,
    error_policy: Union[Unset, None, str] = UNSET,
    output_fields: Union[Unset, None, str] = UNSET,
) -> Response[List["AnnotatedDocument"]]:
    """annotate a binary document with the default annotator of the project

    Args:
        project_name (str):
        inline_labels (Union[Unset, None, bool]):  Default: True.
        inline_label_ids (Union[Unset, None, bool]):  Default: True.
        inline_text (Union[Unset, None, bool]):  Default: True.
        debug (Union[Unset, None, bool]):
        parallelize (Union[Unset, None, bool]):
        error_policy (Union[Unset, None, str]):
        output_fields (Union[Unset, None, str]):
        multipart_data (AnnotateBinaryWithProjectMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['AnnotatedDocument']]
    """

    kwargs = _get_kwargs(
        project_name=project_name,
        client=client,
        multipart_data=multipart_data,
        inline_labels=inline_labels,
        inline_label_ids=inline_label_ids,
        inline_text=inline_text,
        debug=debug,
        parallelize=parallelize,
        error_policy=error_policy,
        output_fields=output_fields,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_name: str,
    *,
    client: Client,
    multipart_data: AnnotateBinaryWithProjectMultipartData,
    inline_labels: Union[Unset, None, bool] = True,
    inline_label_ids: Union[Unset, None, bool] = True,
    inline_text: Union[Unset, None, bool] = True,
    debug: Union[Unset, None, bool] = False,
    parallelize: Union[Unset, None, bool] = False,
    error_policy: Union[Unset, None, str] = UNSET,
    output_fields: Union[Unset, None, str] = UNSET,
) -> Optional[List["AnnotatedDocument"]]:
    """annotate a binary document with the default annotator of the project

    Args:
        project_name (str):
        inline_labels (Union[Unset, None, bool]):  Default: True.
        inline_label_ids (Union[Unset, None, bool]):  Default: True.
        inline_text (Union[Unset, None, bool]):  Default: True.
        debug (Union[Unset, None, bool]):
        parallelize (Union[Unset, None, bool]):
        error_policy (Union[Unset, None, str]):
        output_fields (Union[Unset, None, str]):
        multipart_data (AnnotateBinaryWithProjectMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['AnnotatedDocument']]
    """

    return (
        await asyncio_detailed(
            project_name=project_name,
            client=client,
            multipart_data=multipart_data,
            inline_labels=inline_labels,
            inline_label_ids=inline_label_ids,
            inline_text=inline_text,
            debug=debug,
            parallelize=parallelize,
            error_policy=error_policy,
            output_fields=output_fields,
        )
    ).parsed
