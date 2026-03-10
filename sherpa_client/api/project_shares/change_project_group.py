from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user_group_ref import UserGroupRef
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_name: str,
    *,
    group_name: str,
    delete_existing_group_shares: Union[Unset, bool] = False,
    delete_existing_user_shares: Union[Unset, bool] = False,
    share_with_new_group: Union[Unset, bool] = False,
    read_only_share: Union[Unset, bool] = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["groupName"] = group_name

    params["deleteExistingGroupShares"] = delete_existing_group_shares

    params["deleteExistingUserShares"] = delete_existing_user_shares

    params["shareWithNewGroup"] = share_with_new_group

    params["readOnlyShare"] = read_only_share

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_name}/_chgrp".format(
            project_name=project_name,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[UserGroupRef]:
    if response.status_code == 200:
        response_200 = UserGroupRef.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[UserGroupRef]:
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
    group_name: str,
    delete_existing_group_shares: Union[Unset, bool] = False,
    delete_existing_user_shares: Union[Unset, bool] = False,
    share_with_new_group: Union[Unset, bool] = False,
    read_only_share: Union[Unset, bool] = False,
) -> Response[UserGroupRef]:
    """Change the group of the project

    Args:
        project_name (str):
        group_name (str):
        delete_existing_group_shares (Union[Unset, bool]):  Default: False.
        delete_existing_user_shares (Union[Unset, bool]):  Default: False.
        share_with_new_group (Union[Unset, bool]):  Default: False.
        read_only_share (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserGroupRef]
    """

    kwargs = _get_kwargs(
        project_name=project_name,
        group_name=group_name,
        delete_existing_group_shares=delete_existing_group_shares,
        delete_existing_user_shares=delete_existing_user_shares,
        share_with_new_group=share_with_new_group,
        read_only_share=read_only_share,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    group_name: str,
    delete_existing_group_shares: Union[Unset, bool] = False,
    delete_existing_user_shares: Union[Unset, bool] = False,
    share_with_new_group: Union[Unset, bool] = False,
    read_only_share: Union[Unset, bool] = False,
) -> Optional[UserGroupRef]:
    """Change the group of the project

    Args:
        project_name (str):
        group_name (str):
        delete_existing_group_shares (Union[Unset, bool]):  Default: False.
        delete_existing_user_shares (Union[Unset, bool]):  Default: False.
        share_with_new_group (Union[Unset, bool]):  Default: False.
        read_only_share (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserGroupRef
    """

    return sync_detailed(
        project_name=project_name,
        client=client,
        group_name=group_name,
        delete_existing_group_shares=delete_existing_group_shares,
        delete_existing_user_shares=delete_existing_user_shares,
        share_with_new_group=share_with_new_group,
        read_only_share=read_only_share,
    ).parsed


async def asyncio_detailed(
    project_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    group_name: str,
    delete_existing_group_shares: Union[Unset, bool] = False,
    delete_existing_user_shares: Union[Unset, bool] = False,
    share_with_new_group: Union[Unset, bool] = False,
    read_only_share: Union[Unset, bool] = False,
) -> Response[UserGroupRef]:
    """Change the group of the project

    Args:
        project_name (str):
        group_name (str):
        delete_existing_group_shares (Union[Unset, bool]):  Default: False.
        delete_existing_user_shares (Union[Unset, bool]):  Default: False.
        share_with_new_group (Union[Unset, bool]):  Default: False.
        read_only_share (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UserGroupRef]
    """

    kwargs = _get_kwargs(
        project_name=project_name,
        group_name=group_name,
        delete_existing_group_shares=delete_existing_group_shares,
        delete_existing_user_shares=delete_existing_user_shares,
        share_with_new_group=share_with_new_group,
        read_only_share=read_only_share,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    group_name: str,
    delete_existing_group_shares: Union[Unset, bool] = False,
    delete_existing_user_shares: Union[Unset, bool] = False,
    share_with_new_group: Union[Unset, bool] = False,
    read_only_share: Union[Unset, bool] = False,
) -> Optional[UserGroupRef]:
    """Change the group of the project

    Args:
        project_name (str):
        group_name (str):
        delete_existing_group_shares (Union[Unset, bool]):  Default: False.
        delete_existing_user_shares (Union[Unset, bool]):  Default: False.
        share_with_new_group (Union[Unset, bool]):  Default: False.
        read_only_share (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UserGroupRef
    """

    return (
        await asyncio_detailed(
            project_name=project_name,
            client=client,
            group_name=group_name,
            delete_existing_group_shares=delete_existing_group_shares,
            delete_existing_user_shares=delete_existing_user_shares,
            share_with_new_group=share_with_new_group,
            read_only_share=read_only_share,
        )
    ).parsed
