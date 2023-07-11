from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemMyAccountIdSkillsIdEndpoint import SystemMyAccountIdSkillsIdEndpoint
from pyconnectwise.endpoints.manage.SystemMyAccountIdSkillsCountEndpoint import SystemMyAccountIdSkillsCountEndpoint
from pyconnectwise.models.manage.MemberSkillModel import MemberSkillModel

class SystemMyAccountIdSkillsEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "skills", parent_endpoint=parent_endpoint)
        
        self.count = self.register_child_endpoint(
            SystemMyAccountIdSkillsCountEndpoint(client, parent_endpoint=self)
        )
    
    
    def id(self, id: int) -> SystemMyAccountIdSkillsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized SystemMyAccountIdSkillsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            SystemMyAccountIdSkillsIdEndpoint: The initialized SystemMyAccountIdSkillsIdEndpoint object.
        """
        child = SystemMyAccountIdSkillsIdEndpoint(self.client, parent_endpoint=self)
        child._id = id
        return child
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[MemberSkillModel]:
        """
        Performs a GET request against the /system/myAccount/{parentId}/skills endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[MemberSkillModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            MemberSkillModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> list[MemberSkillModel]:
        """
        Performs a GET request against the /system/myAccount/{parentId}/skills endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[MemberSkillModel]: The parsed response data.
        """
        return self._parse_many(MemberSkillModel, super().make_request("GET", data=data, params=params).json())
        
    def post(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> MemberSkillModel:
        """
        Performs a POST request against the /system/myAccount/{parentId}/skills endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            MemberSkillModel: The parsed response data.
        """
        return self._parse_one(MemberSkillModel, super().make_request("POST", data=data, params=params).json())
        