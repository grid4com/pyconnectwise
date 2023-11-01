from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.TimeWorkrolesIdInfoEndpoint import (
    TimeWorkrolesIdInfoEndpoint,
)
from pyconnectwise.endpoints.manage.TimeWorkrolesIdLocationsEndpoint import (
    TimeWorkrolesIdLocationsEndpoint,
)
from pyconnectwise.endpoints.manage.TimeWorkrolesIdUsagesEndpoint import (
    TimeWorkrolesIdUsagesEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPatchable,
    IPuttable,
)
from pyconnectwise.models.manage import WorkRole
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class TimeWorkrolesIdEndpoint(
    ConnectWiseEndpoint,
    IGettable[WorkRole, ConnectWiseManageRequestParams],
    IPuttable[WorkRole, ConnectWiseManageRequestParams],
    IPatchable[WorkRole, ConnectWiseManageRequestParams],
    IPaginateable[WorkRole, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "{id}", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, WorkRole)
        IPuttable.__init__(self, WorkRole)
        IPatchable.__init__(self, WorkRole)
        IPaginateable.__init__(self, WorkRole)

        self.usages = self._register_child_endpoint(
            TimeWorkrolesIdUsagesEndpoint(client, parent_endpoint=self)
        )
        self.locations = self._register_child_endpoint(
            TimeWorkrolesIdLocationsEndpoint(client, parent_endpoint=self)
        )
        self.info = self._register_child_endpoint(
            TimeWorkrolesIdInfoEndpoint(client, parent_endpoint=self)
        )

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[WorkRole]:
        """
        Performs a GET request against the /time/workRoles/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[WorkRole]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            WorkRole,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> WorkRole:
        """
        Performs a GET request against the /time/workRoles/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkRole: The parsed response data.
        """
        return self._parse_one(
            WorkRole, super()._make_request("GET", data=data, params=params).json()
        )

    def delete(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> None:
        """
        Performs a DELETE request against the /time/workRoles/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        """
        super()._make_request("DELETE", data=data, params=params)

    def put(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> WorkRole:
        """
        Performs a PUT request against the /time/workRoles/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkRole: The parsed response data.
        """
        return self._parse_one(
            WorkRole, super()._make_request("PUT", data=data, params=params).json()
        )

    def patch(
        self,
        data: PatchRequestData,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> WorkRole:
        """
        Performs a PATCH request against the /time/workRoles/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkRole: The parsed response data.
        """
        return self._parse_one(
            WorkRole, super()._make_request("PATCH", data=data, params=params).json()
        )
