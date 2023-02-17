from http import HTTPStatus
from io import BytesIO
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.deprecated_annotate_format_binary_with_plan_ref_multipart_data import (
    DeprecatedAnnotateFormatBinaryWithPlanRefMultipartData,
)
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    project_name: str,
    plan_name: str,
    *,
    client: Client,
    multipart_data: DeprecatedAnnotateFormatBinaryWithPlanRefMultipartData,
    inline_labels: Union[Unset, None, bool] = True,
    inline_label_ids: Union[Unset, None, bool] = True,
    inline_text: Union[Unset, None, bool] = True,
    debug: Union[Unset, None, bool] = False,
    parallelize: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/projects/{projectName}/plans/{planName}/_annotate_format_binary".format(
        client.base_url, projectName=project_name, planName=plan_name
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["inlineLabels"] = inline_labels

    params["inlineLabelIds"] = inline_label_ids

    params["inlineText"] = inline_text

    params["debug"] = debug

    params["parallelize"] = parallelize

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


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[File]:
    if response.status_code == HTTPStatus.OK:
        response_200 = File(payload=BytesIO(response.json()))

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[File]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_name: str,
    plan_name: str,
    *,
    client: Client,
    multipart_data: DeprecatedAnnotateFormatBinaryWithPlanRefMultipartData,
    inline_labels: Union[Unset, None, bool] = True,
    inline_label_ids: Union[Unset, None, bool] = True,
    inline_text: Union[Unset, None, bool] = True,
    debug: Union[Unset, None, bool] = False,
    parallelize: Union[Unset, None, bool] = False,
) -> Response[File]:
    """annotate a binary document with multiple annotators and return a formatted result (replaced with
    /projects/{projectName}/annotators/{annotator}/_annotate_format_binary)

    Args:
        project_name (str):
        plan_name (str):
        inline_labels (Union[Unset, None, bool]):  Default: True.
        inline_label_ids (Union[Unset, None, bool]):  Default: True.
        inline_text (Union[Unset, None, bool]):  Default: True.
        debug (Union[Unset, None, bool]):
        parallelize (Union[Unset, None, bool]):
        multipart_data (DeprecatedAnnotateFormatBinaryWithPlanRefMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        project_name=project_name,
        plan_name=plan_name,
        client=client,
        multipart_data=multipart_data,
        inline_labels=inline_labels,
        inline_label_ids=inline_label_ids,
        inline_text=inline_text,
        debug=debug,
        parallelize=parallelize,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_name: str,
    plan_name: str,
    *,
    client: Client,
    multipart_data: DeprecatedAnnotateFormatBinaryWithPlanRefMultipartData,
    inline_labels: Union[Unset, None, bool] = True,
    inline_label_ids: Union[Unset, None, bool] = True,
    inline_text: Union[Unset, None, bool] = True,
    debug: Union[Unset, None, bool] = False,
    parallelize: Union[Unset, None, bool] = False,
) -> Optional[File]:
    """annotate a binary document with multiple annotators and return a formatted result (replaced with
    /projects/{projectName}/annotators/{annotator}/_annotate_format_binary)

    Args:
        project_name (str):
        plan_name (str):
        inline_labels (Union[Unset, None, bool]):  Default: True.
        inline_label_ids (Union[Unset, None, bool]):  Default: True.
        inline_text (Union[Unset, None, bool]):  Default: True.
        debug (Union[Unset, None, bool]):
        parallelize (Union[Unset, None, bool]):
        multipart_data (DeprecatedAnnotateFormatBinaryWithPlanRefMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    return sync_detailed(
        project_name=project_name,
        plan_name=plan_name,
        client=client,
        multipart_data=multipart_data,
        inline_labels=inline_labels,
        inline_label_ids=inline_label_ids,
        inline_text=inline_text,
        debug=debug,
        parallelize=parallelize,
    ).parsed


async def asyncio_detailed(
    project_name: str,
    plan_name: str,
    *,
    client: Client,
    multipart_data: DeprecatedAnnotateFormatBinaryWithPlanRefMultipartData,
    inline_labels: Union[Unset, None, bool] = True,
    inline_label_ids: Union[Unset, None, bool] = True,
    inline_text: Union[Unset, None, bool] = True,
    debug: Union[Unset, None, bool] = False,
    parallelize: Union[Unset, None, bool] = False,
) -> Response[File]:
    """annotate a binary document with multiple annotators and return a formatted result (replaced with
    /projects/{projectName}/annotators/{annotator}/_annotate_format_binary)

    Args:
        project_name (str):
        plan_name (str):
        inline_labels (Union[Unset, None, bool]):  Default: True.
        inline_label_ids (Union[Unset, None, bool]):  Default: True.
        inline_text (Union[Unset, None, bool]):  Default: True.
        debug (Union[Unset, None, bool]):
        parallelize (Union[Unset, None, bool]):
        multipart_data (DeprecatedAnnotateFormatBinaryWithPlanRefMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        project_name=project_name,
        plan_name=plan_name,
        client=client,
        multipart_data=multipart_data,
        inline_labels=inline_labels,
        inline_label_ids=inline_label_ids,
        inline_text=inline_text,
        debug=debug,
        parallelize=parallelize,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_name: str,
    plan_name: str,
    *,
    client: Client,
    multipart_data: DeprecatedAnnotateFormatBinaryWithPlanRefMultipartData,
    inline_labels: Union[Unset, None, bool] = True,
    inline_label_ids: Union[Unset, None, bool] = True,
    inline_text: Union[Unset, None, bool] = True,
    debug: Union[Unset, None, bool] = False,
    parallelize: Union[Unset, None, bool] = False,
) -> Optional[File]:
    """annotate a binary document with multiple annotators and return a formatted result (replaced with
    /projects/{projectName}/annotators/{annotator}/_annotate_format_binary)

    Args:
        project_name (str):
        plan_name (str):
        inline_labels (Union[Unset, None, bool]):  Default: True.
        inline_label_ids (Union[Unset, None, bool]):  Default: True.
        inline_text (Union[Unset, None, bool]):  Default: True.
        debug (Union[Unset, None, bool]):
        parallelize (Union[Unset, None, bool]):
        multipart_data (DeprecatedAnnotateFormatBinaryWithPlanRefMultipartData):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    return (
        await asyncio_detailed(
            project_name=project_name,
            plan_name=plan_name,
            client=client,
            multipart_data=multipart_data,
            inline_labels=inline_labels,
            inline_label_ids=inline_label_ids,
            inline_text=inline_text,
            debug=debug,
            parallelize=parallelize,
        )
    ).parsed