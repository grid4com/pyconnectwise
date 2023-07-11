from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.FinanceAgreementTypesIdWorkrolesIdEndpoint import FinanceAgreementTypesIdWorkrolesIdEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementTypesIdWorkrolesCountEndpoint import FinanceAgreementTypesIdWorkrolesCountEndpoint
from pyconnectwise.endpoints.manage.FinanceAgreementTypesIdWorkrolesInfoEndpoint import FinanceAgreementTypesIdWorkrolesInfoEndpoint
from pyconnectwise.models.manage.AgreementTypeWorkRoleModel import AgreementTypeWorkRoleModel

class FinanceAgreementTypesIdWorkrolesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "workroles", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            FinanceAgreementTypesIdWorkrolesCountEndpoint(client, parent_endpoint=self)
        )
        self.info = self.register_child_endpoint(
            FinanceAgreementTypesIdWorkrolesInfoEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> FinanceAgreementTypesIdWorkrolesIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized FinanceAgreementTypesIdWorkrolesIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            FinanceAgreementTypesIdWorkrolesIdEndpoint: The initialized FinanceAgreementTypesIdWorkrolesIdEndpoint object.
        """
        child = FinanceAgreementTypesIdWorkrolesIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[AgreementTypeWorkRoleModel]:
        """
        Performs a GET request against the /finance/agreementTypes/{parentId}/workroles endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[AgreementTypeWorkRoleModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            AgreementTypeWorkRoleModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[AgreementTypeWorkRoleModel]:
        """
        Performs a GET request against the /finance/agreementTypes/{parentId}/workroles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[AgreementTypeWorkRoleModel]: The parsed response data.
        """
        return self._parse_many(AgreementTypeWorkRoleModel, super().make_request("GET", data=data, params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> AgreementTypeWorkRoleModel:
        """
        Performs a POST request against the /finance/agreementTypes/{parentId}/workroles endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            AgreementTypeWorkRoleModel: The parsed response data.
        """
        return self._parse_one(AgreementTypeWorkRoleModel, super().make_request("POST", data=data, params=params).json())
        