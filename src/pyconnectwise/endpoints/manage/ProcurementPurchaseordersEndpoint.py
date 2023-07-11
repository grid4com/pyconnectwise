from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.ProcurementPurchaseordersIdEndpoint import ProcurementPurchaseordersIdEndpoint
from pyconnectwise.endpoints.manage.ProcurementPurchaseordersCountEndpoint import ProcurementPurchaseordersCountEndpoint
from pyconnectwise.models.manage.PurchaseOrderModel import PurchaseOrderModel

class ProcurementPurchaseordersEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "purchaseorders", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            ProcurementPurchaseordersCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> ProcurementPurchaseordersIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ProcurementPurchaseordersIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ProcurementPurchaseordersIdEndpoint: The initialized ProcurementPurchaseordersIdEndpoint object.
        """
        child = ProcurementPurchaseordersIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[PurchaseOrderModel]:
        """
        Performs a GET request against the /procurement/purchaseorders endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[PurchaseOrderModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            PurchaseOrderModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[PurchaseOrderModel]:
        """
        Performs a GET request against the /procurement/purchaseorders endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[PurchaseOrderModel]: The parsed response data.
        """
        return self._parse_many(PurchaseOrderModel, super().make_request("GET", data=data, params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> PurchaseOrderModel:
        """
        Performs a POST request against the /procurement/purchaseorders endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PurchaseOrderModel: The parsed response data.
        """
        return self._parse_one(PurchaseOrderModel, super().make_request("POST", data=data, params=params).json())
        