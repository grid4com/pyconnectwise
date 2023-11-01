from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.CompanyContactsIdCommunicationsCountEndpoint import (
    CompanyContactsIdCommunicationsCountEndpoint,
)
from pyconnectwise.endpoints.manage.CompanyContactsIdCommunicationsIdEndpoint import (
    CompanyContactsIdCommunicationsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import ContactCommunication
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class CompanyContactsIdCommunicationsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[ContactCommunication], ConnectWiseManageRequestParams],
    IPostable[ContactCommunication, ConnectWiseManageRequestParams],
    IPaginateable[ContactCommunication, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "communications", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[ContactCommunication])
        IPostable.__init__(self, ContactCommunication)
        IPaginateable.__init__(self, ContactCommunication)

        self.count = self._register_child_endpoint(
            CompanyContactsIdCommunicationsCountEndpoint(client, parent_endpoint=self)
        )

    def id(self, id: int) -> CompanyContactsIdCommunicationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized CompanyContactsIdCommunicationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            CompanyContactsIdCommunicationsIdEndpoint: The initialized CompanyContactsIdCommunicationsIdEndpoint object.
        """
        child = CompanyContactsIdCommunicationsIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[ContactCommunication]:
        """
        Performs a GET request against the /company/contacts/{id}/communications endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ContactCommunication]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            ContactCommunication,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[ContactCommunication]:
        """
        Performs a GET request against the /company/contacts/{id}/communications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[ContactCommunication]: The parsed response data.
        """
        return self._parse_many(
            ContactCommunication,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> ContactCommunication:
        """
        Performs a POST request against the /company/contacts/{id}/communications endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ContactCommunication: The parsed response data.
        """
        return self._parse_one(
            ContactCommunication,
            super()._make_request("POST", data=data, params=params).json(),
        )
