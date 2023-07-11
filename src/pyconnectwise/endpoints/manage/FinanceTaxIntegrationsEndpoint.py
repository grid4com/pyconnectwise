from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceTaxIntegrationsIdEndpoint import FinanceTaxIntegrationsIdEndpoint
from pyconnectwise.endpoints.manage.FinanceTaxIntegrationsCountEndpoint import FinanceTaxIntegrationsCountEndpoint
from pyconnectwise.models.manage.TaxIntegrationModel import TaxIntegrationModel

class FinanceTaxIntegrationsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "taxIntegrations", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceTaxIntegrationsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceTaxIntegrationsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceTaxIntegrationsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceTaxIntegrationsIdEndpoint: The initialized FinanceTaxIntegrationsIdEndpoint object.
        """
        child = FinanceTaxIntegrationsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[TaxIntegrationModel]:
        """
        Performs a GET request against the /finance/taxIntegrations endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[TaxIntegrationModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            TaxIntegrationModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[TaxIntegrationModel]:
        """
        Performs a GET request against the /finance/taxIntegrations endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[TaxIntegrationModel]: The parsed response data.
        """
        return self._parse_many(TaxIntegrationModel, super().make_request("GET", data=data, params=params).json())
        