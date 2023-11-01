from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceBoardsIdSubtypesIdInfoEndpoint import (
    ServiceBoardsIdSubtypesIdInfoEndpoint,
)
from pyconnectwise.endpoints.manage.ServiceBoardsIdSubtypesIdUsagesEndpoint import (
    ServiceBoardsIdSubtypesIdUsagesEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPatchable,
    IPuttable,
)
from pyconnectwise.models.manage import BoardSubType
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class ServiceBoardsIdSubtypesIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[BoardSubType, ConnectWiseManageRequestParams],
    IPuttable[BoardSubType, ConnectWiseManageRequestParams],
    IPatchable[BoardSubType, ConnectWiseManageRequestParams],
    IPaginateable[BoardSubType, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, BoardSubType)
        IPuttable.__init__(self, BoardSubType)
        IPatchable.__init__(self, BoardSubType)
        IPaginateable.__init__(self, BoardSubType)

        self.usages = self._register_child_endpoint(
            ServiceBoardsIdSubtypesIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            ServiceBoardsIdSubtypesIdInfoEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[BoardSubType]:
        """
        Performs a GET request against the /service/boards/{id}/subtypes/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[BoardSubType]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            BoardSubType,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> BoardSubType:
        """
        Performs a GET request against the /service/boards/{id}/subtypes/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardSubType: The parsed response data.
        """
        return self._parse_one(
            BoardSubType, super()._make_request("GET", data=data, params=params).json()
        )

    def delete(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> None:
        """
        Performs a DELETE request against the /service/boards/{id}/subtypes/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> BoardSubType:
        """
        Performs a PUT request against the /service/boards/{id}/subtypes/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardSubType: The parsed response data.
        """
        return self._parse_one(
            BoardSubType, super()._make_request("PUT", data=data, params=params).json()
        )

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> BoardSubType:
        """
        Performs a PATCH request against the /service/boards/{id}/subtypes/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            BoardSubType: The parsed response data.
        """
        return self._parse_one(
            BoardSubType,
            super()._make_request("PATCH", data=data, params=params).json(),
        )
