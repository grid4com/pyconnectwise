from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.responses.paginated_response import PaginatedResponse
from typing import Any
from pyconnectwise.endpoints.manage.SystemWorkflowsIdEventsIdActionsEndpoint import SystemWorkflowsIdEventsIdActionsEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsIdEventsIdCopyEndpoint import SystemWorkflowsIdEventsIdCopyEndpoint
from pyconnectwise.endpoints.manage.SystemWorkflowsIdEventsIdTestEndpoint import SystemWorkflowsIdEventsIdTestEndpoint
from pyconnectwise.models.manage.WorkflowEventModel import WorkflowEventModel

class SystemWorkflowsIdEventsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)
        
        self.actions = self.register_child_endpoint(
            SystemWorkflowsIdEventsIdActionsEndpoint(client, parent_endpoint=self)
        )
        self.copy = self.register_child_endpoint(
            SystemWorkflowsIdEventsIdCopyEndpoint(client, parent_endpoint=self)
        )
        self.test = self.register_child_endpoint(
            SystemWorkflowsIdEventsIdTestEndpoint(client, parent_endpoint=self)
        )
    
    
    def paginated(self, page: int, page_size: int, params: dict[str, int | str] = {}) -> PaginatedResponse[WorkflowEventModel]:
        """
        Performs a GET request against the /system/workflows/{parentId}/events/{id} endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[WorkflowEventModel]: The initialized PaginatedResponse object.
        """
        params["page"] = page
        params["pageSize"] = page_size
        return PaginatedResponse(
            super().make_request(
                "GET",
                params=params
            ),
            WorkflowEventModel,
            self,
            page_size,
        )
    
    def get(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> WorkflowEventModel:
        """
        Performs a GET request against the /system/workflows/{parentId}/events/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkflowEventModel: The parsed response data.
        """
        return self._parse_one(WorkflowEventModel, super().make_request("GET", data=data, params=params).json())
        
    def delete(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> GenericMessageModel:
        """
        Performs a DELETE request against the /system/workflows/{parentId}/events/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            GenericMessageModel: The parsed response data.
        """
        return self._parse_one(GenericMessageModel, super().make_request("DELETE", data=data, params=params).json())
        
    def put(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> WorkflowEventModel:
        """
        Performs a PUT request against the /system/workflows/{parentId}/events/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkflowEventModel: The parsed response data.
        """
        return self._parse_one(WorkflowEventModel, super().make_request("PUT", data=data, params=params).json())
        
    def patch(self, data: dict[str, Any] = {}, params: dict[str, int | str] = {}) -> WorkflowEventModel:
        """
        Performs a PATCH request against the /system/workflows/{parentId}/events/{id} endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            WorkflowEventModel: The parsed response data.
        """
        return self._parse_one(WorkflowEventModel, super().make_request("PATCH", data=data, params=params).json())
        