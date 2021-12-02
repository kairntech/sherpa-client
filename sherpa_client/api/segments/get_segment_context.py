from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.get_segment_context_context_output import GetSegmentContextContextOutput
from ...models.segment_contexts import SegmentContexts
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_name: str,
    *,
    client: Client,
    document_identifier: str,
    segment_start: int,
    from_before: Union[Unset, None, int] = 0,
    size_before: Union[Unset, None, int] = 1,
    from_after: Union[Unset, None, int] = 0,
    size_after: Union[Unset, None, int] = 1,
    context_output: Union[Unset, None, GetSegmentContextContextOutput] = GetSegmentContextContextOutput.SEGMENTS,
    include_annotations: Union[Unset, None, bool] = False,
    html_version: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/projects/{projectName}/segments/_context".format(client.base_url, projectName=project_name)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_context_output: Union[Unset, None, str] = UNSET
    if not isinstance(context_output, Unset):
        json_context_output = context_output.value if context_output else None

    params: Dict[str, Any] = {
        "documentIdentifier": document_identifier,
        "segmentStart": segment_start,
        "fromBefore": from_before,
        "sizeBefore": size_before,
        "fromAfter": from_after,
        "sizeAfter": size_after,
        "contextOutput": json_context_output,
        "includeAnnotations": include_annotations,
        "htmlVersion": html_version,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[SegmentContexts]:
    if response.status_code == 200:
        response_200 = SegmentContexts.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[SegmentContexts]:
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
    document_identifier: str,
    segment_start: int,
    from_before: Union[Unset, None, int] = 0,
    size_before: Union[Unset, None, int] = 1,
    from_after: Union[Unset, None, int] = 0,
    size_after: Union[Unset, None, int] = 1,
    context_output: Union[Unset, None, GetSegmentContextContextOutput] = GetSegmentContextContextOutput.SEGMENTS,
    include_annotations: Union[Unset, None, bool] = False,
    html_version: Union[Unset, None, bool] = False,
) -> Response[SegmentContexts]:
    kwargs = _get_kwargs(
        project_name=project_name,
        client=client,
        document_identifier=document_identifier,
        segment_start=segment_start,
        from_before=from_before,
        size_before=size_before,
        from_after=from_after,
        size_after=size_after,
        context_output=context_output,
        include_annotations=include_annotations,
        html_version=html_version,
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
    document_identifier: str,
    segment_start: int,
    from_before: Union[Unset, None, int] = 0,
    size_before: Union[Unset, None, int] = 1,
    from_after: Union[Unset, None, int] = 0,
    size_after: Union[Unset, None, int] = 1,
    context_output: Union[Unset, None, GetSegmentContextContextOutput] = GetSegmentContextContextOutput.SEGMENTS,
    include_annotations: Union[Unset, None, bool] = False,
    html_version: Union[Unset, None, bool] = False,
) -> Optional[SegmentContexts]:
    """ """

    return sync_detailed(
        project_name=project_name,
        client=client,
        document_identifier=document_identifier,
        segment_start=segment_start,
        from_before=from_before,
        size_before=size_before,
        from_after=from_after,
        size_after=size_after,
        context_output=context_output,
        include_annotations=include_annotations,
        html_version=html_version,
    ).parsed


async def asyncio_detailed(
    project_name: str,
    *,
    client: Client,
    document_identifier: str,
    segment_start: int,
    from_before: Union[Unset, None, int] = 0,
    size_before: Union[Unset, None, int] = 1,
    from_after: Union[Unset, None, int] = 0,
    size_after: Union[Unset, None, int] = 1,
    context_output: Union[Unset, None, GetSegmentContextContextOutput] = GetSegmentContextContextOutput.SEGMENTS,
    include_annotations: Union[Unset, None, bool] = False,
    html_version: Union[Unset, None, bool] = False,
) -> Response[SegmentContexts]:
    kwargs = _get_kwargs(
        project_name=project_name,
        client=client,
        document_identifier=document_identifier,
        segment_start=segment_start,
        from_before=from_before,
        size_before=size_before,
        from_after=from_after,
        size_after=size_after,
        context_output=context_output,
        include_annotations=include_annotations,
        html_version=html_version,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    project_name: str,
    *,
    client: Client,
    document_identifier: str,
    segment_start: int,
    from_before: Union[Unset, None, int] = 0,
    size_before: Union[Unset, None, int] = 1,
    from_after: Union[Unset, None, int] = 0,
    size_after: Union[Unset, None, int] = 1,
    context_output: Union[Unset, None, GetSegmentContextContextOutput] = GetSegmentContextContextOutput.SEGMENTS,
    include_annotations: Union[Unset, None, bool] = False,
    html_version: Union[Unset, None, bool] = False,
) -> Optional[SegmentContexts]:
    """ """

    return (
        await asyncio_detailed(
            project_name=project_name,
            client=client,
            document_identifier=document_identifier,
            segment_start=segment_start,
            from_before=from_before,
            size_before=size_before,
            from_after=from_after,
            size_after=size_after,
            context_output=context_output,
            include_annotations=include_annotations,
            html_version=html_version,
        )
    ).parsed
