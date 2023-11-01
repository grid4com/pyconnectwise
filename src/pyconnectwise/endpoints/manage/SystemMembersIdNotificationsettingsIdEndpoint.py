from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPatchable,
    IPuttable,
)
from pyconnectwise.models.manage import MemberNotificationSetting
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class SystemMembersIdNotificationsettingsIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[MemberNotificationSetting, ConnectWiseManageRequestParams],
    IPuttable[MemberNotificationSetting, ConnectWiseManageRequestParams],
    IPatchable[MemberNotificationSetting, ConnectWiseManageRequestParams],
    IPaginateable[MemberNotificationSetting, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, MemberNotificationSetting)
        IPuttable.__init__(self, MemberNotificationSetting)
        IPatchable.__init__(self, MemberNotificationSetting)
        IPaginateable.__init__(self, MemberNotificationSetting)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[MemberNotificationSetting]:
        """
        Performs a GET request against the /system/members/{id}/notificationSettings/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MemberNotificationSetting]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            MemberNotificationSetting,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> MemberNotificationSetting:
        """
        Performs a GET request against the /system/members/{id}/notificationSettings/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MemberNotificationSetting: The parsed response data.
        """
        return self._parse_one(
            MemberNotificationSetting,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def delete(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> None:
        """
        Performs a DELETE request against the /system/members/{id}/notificationSettings/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> MemberNotificationSetting:
        """
        Performs a PUT request against the /system/members/{id}/notificationSettings/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MemberNotificationSetting: The parsed response data.
        """
        return self._parse_one(
            MemberNotificationSetting,
            super()._make_request("PUT", data=data, params=params).json(),
        )

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> MemberNotificationSetting:
        """
        Performs a PATCH request against the /system/members/{id}/notificationSettings/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MemberNotificationSetting: The parsed response data.
        """
        return self._parse_one(
            MemberNotificationSetting,
            super()._make_request("PATCH", data=data, params=params).json(),
        )
