from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.get_services_distinct_values_response_200_item import GetServicesDistinctValuesResponse200Item
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    field: str,
    name: Union[Unset, None, str] = "",
    api: Union[Unset, None, str] = "",
    engine: Union[Unset, None, str] = "",
    function: Union[Unset, None, str] = "",
    language: Union[Unset, None, str] = "",
    type: Union[Unset, None, str] = "",
    nature: Union[Unset, None, str] = "",
    version: Union[Unset, None, str] = "",
    term_importer: Union[Unset, None, str] = "",
    annotator: Union[Unset, None, str] = "",
    processor: Union[Unset, None, str] = "",
    formatter: Union[Unset, None, str] = "",
    converter: Union[Unset, None, str] = "",
) -> Dict[str, Any]:
    url = "{}/service_values".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "field": field,
        "name": name,
        "api": api,
        "engine": engine,
        "function": function,
        "language": language,
        "type": type,
        "nature": nature,
        "version": version,
        "termImporter": term_importer,
        "annotator": annotator,
        "processor": processor,
        "formatter": formatter,
        "converter": converter,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[GetServicesDistinctValuesResponse200Item]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetServicesDistinctValuesResponse200Item.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[GetServicesDistinctValuesResponse200Item]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    field: str,
    name: Union[Unset, None, str] = "",
    api: Union[Unset, None, str] = "",
    engine: Union[Unset, None, str] = "",
    function: Union[Unset, None, str] = "",
    language: Union[Unset, None, str] = "",
    type: Union[Unset, None, str] = "",
    nature: Union[Unset, None, str] = "",
    version: Union[Unset, None, str] = "",
    term_importer: Union[Unset, None, str] = "",
    annotator: Union[Unset, None, str] = "",
    processor: Union[Unset, None, str] = "",
    formatter: Union[Unset, None, str] = "",
    converter: Union[Unset, None, str] = "",
) -> Response[List[GetServicesDistinctValuesResponse200Item]]:
    kwargs = _get_kwargs(
        client=client,
        field=field,
        name=name,
        api=api,
        engine=engine,
        function=function,
        language=language,
        type=type,
        nature=nature,
        version=version,
        term_importer=term_importer,
        annotator=annotator,
        processor=processor,
        formatter=formatter,
        converter=converter,
    )

    response = httpx.get(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    field: str,
    name: Union[Unset, None, str] = "",
    api: Union[Unset, None, str] = "",
    engine: Union[Unset, None, str] = "",
    function: Union[Unset, None, str] = "",
    language: Union[Unset, None, str] = "",
    type: Union[Unset, None, str] = "",
    nature: Union[Unset, None, str] = "",
    version: Union[Unset, None, str] = "",
    term_importer: Union[Unset, None, str] = "",
    annotator: Union[Unset, None, str] = "",
    processor: Union[Unset, None, str] = "",
    formatter: Union[Unset, None, str] = "",
    converter: Union[Unset, None, str] = "",
) -> Optional[List[GetServicesDistinctValuesResponse200Item]]:
    """ """

    return sync_detailed(
        client=client,
        field=field,
        name=name,
        api=api,
        engine=engine,
        function=function,
        language=language,
        type=type,
        nature=nature,
        version=version,
        term_importer=term_importer,
        annotator=annotator,
        processor=processor,
        formatter=formatter,
        converter=converter,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    field: str,
    name: Union[Unset, None, str] = "",
    api: Union[Unset, None, str] = "",
    engine: Union[Unset, None, str] = "",
    function: Union[Unset, None, str] = "",
    language: Union[Unset, None, str] = "",
    type: Union[Unset, None, str] = "",
    nature: Union[Unset, None, str] = "",
    version: Union[Unset, None, str] = "",
    term_importer: Union[Unset, None, str] = "",
    annotator: Union[Unset, None, str] = "",
    processor: Union[Unset, None, str] = "",
    formatter: Union[Unset, None, str] = "",
    converter: Union[Unset, None, str] = "",
) -> Response[List[GetServicesDistinctValuesResponse200Item]]:
    kwargs = _get_kwargs(
        client=client,
        field=field,
        name=name,
        api=api,
        engine=engine,
        function=function,
        language=language,
        type=type,
        nature=nature,
        version=version,
        term_importer=term_importer,
        annotator=annotator,
        processor=processor,
        formatter=formatter,
        converter=converter,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    field: str,
    name: Union[Unset, None, str] = "",
    api: Union[Unset, None, str] = "",
    engine: Union[Unset, None, str] = "",
    function: Union[Unset, None, str] = "",
    language: Union[Unset, None, str] = "",
    type: Union[Unset, None, str] = "",
    nature: Union[Unset, None, str] = "",
    version: Union[Unset, None, str] = "",
    term_importer: Union[Unset, None, str] = "",
    annotator: Union[Unset, None, str] = "",
    processor: Union[Unset, None, str] = "",
    formatter: Union[Unset, None, str] = "",
    converter: Union[Unset, None, str] = "",
) -> Optional[List[GetServicesDistinctValuesResponse200Item]]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            field=field,
            name=name,
            api=api,
            engine=engine,
            function=function,
            language=language,
            type=type,
            nature=nature,
            version=version,
            term_importer=term_importer,
            annotator=annotator,
            processor=processor,
            formatter=formatter,
            converter=converter,
        )
    ).parsed
