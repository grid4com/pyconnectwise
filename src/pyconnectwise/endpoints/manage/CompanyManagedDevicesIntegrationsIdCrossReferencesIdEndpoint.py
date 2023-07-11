from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.models.manage.ManagedDevicesIntegrationCrossReferenceModel import ManagedDevicesIntegrationCrossReferenceModel

class CompanyManagedDevicesIntegrationsIdCrossReferencesIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[ManagedDevicesIntegrationCrossReferenceModel]:
        """
        Performs a GET request against the /company/managedDevicesIntegrations/{parentId}/crossReferences/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[ManagedDevicesIntegrationCrossReferenceModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            ManagedDevicesIntegrationCrossReferenceModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ManagedDevicesIntegrationCrossReferenceModel:
        """
        Performs a GET request against the /company/managedDevicesIntegrations/{parentId}/crossReferences/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagedDevicesIntegrationCrossReferenceModel: The parsed response data.
        """
        return self._parse_one(ManagedDevicesIntegrationCrossReferenceModel, super().make_request("GET", data=data, params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ManagedDevicesIntegrationCrossReferenceModel:
        """
        Performs a PUT request against the /company/managedDevicesIntegrations/{parentId}/crossReferences/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagedDevicesIntegrationCrossReferenceModel: The parsed response data.
        """
        return self._parse_one(ManagedDevicesIntegrationCrossReferenceModel, super().make_request("PUT", data=data, params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ManagedDevicesIntegrationCrossReferenceModel:
        """
        Performs a PATCH request against the /company/managedDevicesIntegrations/{parentId}/crossReferences/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagedDevicesIntegrationCrossReferenceModel: The parsed response data.
        """
        return self._parse_one(ManagedDevicesIntegrationCrossReferenceModel, super().make_request("PATCH", data=data, params=params).json())
        
    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> ManagedDevicesIntegrationCrossReferenceModel:
        """
        Performs a DELETE request against the /company/managedDevicesIntegrations/{parentId}/crossReferences/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            ManagedDevicesIntegrationCrossReferenceModel: The parsed response data.
        """
        return self._parse_one(ManagedDevicesIntegrationCrossReferenceModel, super().make_request("DELETE", data=data, params=params).json())
        