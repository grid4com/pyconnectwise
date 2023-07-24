from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.SalesOrdersStatusesInfoCountEndpoint import SalesOrdersStatusesInfoCountEndpoint
from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.models.manage import OrderStatusInfo
from pyconnectwise.responses.paginated_response import PaginatedResponse


class SalesOrdersStatusesInfoEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "info", parent_endpoint=parent_endpoint)

        self.count = self._register_child_endpoint(SalesOrdersStatusesInfoCountEndpoint(client, parent_endpoint=self))

    def paginated(
        self, page: int, page_size: int, params: dict[str, int | str] = {}
    ) -> PaginatedResponse[OrderStatusInfo]:
        """
        Performs a GET request against the /sales/orders/statuses/info endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[OrderStatusInfo]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            OrderStatusInfo,
            self,
            page,
            page_size,
        )

    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[OrderStatusInfo]:
        """
        Performs a GET request against the /sales/orders/statuses/info endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[OrderStatusInfo]: The parsed response data.
        """
        return self._parse_many(OrderStatusInfo, super()._make_request("GET", data=data, params=params).json())