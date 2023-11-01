from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.FinanceAccountingUnpostedprocurementCountEndpoint import (
    FinanceAccountingUnpostedprocurementCountEndpoint,
)
from pyconnectwise.endpoints.manage.FinanceAccountingUnpostedprocurementIdEndpoint import (
    FinanceAccountingUnpostedprocurementIdEndpoint,
)
from pyconnectwise.interfaces import (
    IDeleteable,
    IGettable,
    IPaginateable,
    IPatchable,
    IPostable,
    IPuttable,
)
from pyconnectwise.models.manage import UnpostedProcurement
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
    ConnectWiseManageRequestParams,
    PatchRequestData,
)


class FinanceAccountingUnpostedprocurementEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[UnpostedProcurement], ConnectWiseManageRequestParams],
    IPaginateable[UnpostedProcurement, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "unpostedprocurement", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[UnpostedProcurement])
        IPaginateable.__init__(self, UnpostedProcurement)

        self.count = self._register_child_endpoint(
            FinanceAccountingUnpostedprocurementCountEndpoint(
                client, parent_endpoint=self
            )
        )

    def id(self, id: int) -> FinanceAccountingUnpostedprocurementIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAccountingUnpostedprocurementIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAccountingUnpostedprocurementIdEndpoint: The initialized FinanceAccountingUnpostedprocurementIdEndpoint object.
        """
        child = FinanceAccountingUnpostedprocurementIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[UnpostedProcurement]:
        """
        Performs a GET request against the /finance/accounting/unpostedprocurement endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[UnpostedProcurement]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            UnpostedProcurement,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[UnpostedProcurement]:
        """
        Performs a GET request against the /finance/accounting/unpostedprocurement endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[UnpostedProcurement]: The parsed response data.
        """
        return self._parse_many(
            UnpostedProcurement,
            super()._make_request("GET", data=data, params=params).json(),
        )
