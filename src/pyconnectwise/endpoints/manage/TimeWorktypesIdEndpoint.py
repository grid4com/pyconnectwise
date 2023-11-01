from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.TimeWorktypesIdInfoEndpoint import (
    TimeWorktypesIdInfoEndpoint,
)
from pyconnectwise.endpoints.manage.TimeWorktypesIdUsagesEndpoint import (
    TimeWorktypesIdUsagesEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import WorkType
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class TimeWorktypesIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[WorkType, ConnectWiseManageRequestParams],
    IPuttable[WorkType, ConnectWiseManageRequestParams],
    IPatchable[WorkType, ConnectWiseManageRequestParams],
    IPaginateable[WorkType, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, WorkType)
        IPuttable.__init__(self, WorkType)
        IPatchable.__init__(self, WorkType)
        IPaginateable.__init__(self, WorkType)

        self.usages = self._register_child_endpoint(
            TimeWorktypesIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            TimeWorktypesIdInfoEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[WorkType]:
        """
        Performs a GET request against the /time/workTypes/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[WorkType]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            WorkType,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> WorkType:
        """
        Performs a GET request against the /time/workTypes/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkType: The parsed response data.
        """
        return self._parse_one(
            WorkType, super()._make_request("GET", data=data, params=params).json()
        )

    def delete(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> None:
        """
        Performs a DELETE request against the /time/workTypes/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> WorkType:
        """
        Performs a PUT request against the /time/workTypes/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkType: The parsed response data.
        """
        return self._parse_one(
            WorkType, super()._make_request("PUT", data=data, params=params).json()
        )

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> WorkType:
        """
        Performs a PATCH request against the /time/workTypes/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkType: The parsed response data.
        """
        return self._parse_one(
            WorkType, super()._make_request("PATCH", data=data, params=params).json()
        )
