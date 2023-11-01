from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ServiceSurveysIdQuestionsIdOptionsCountEndpoint import (
    ServiceSurveysIdQuestionsIdOptionsCountEndpoint,
)
from pyconnectwise.endpoints.manage.ServiceSurveysIdQuestionsIdOptionsIdEndpoint import (
    ServiceSurveysIdQuestionsIdOptionsIdEndpoint,
)
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.manage import SurveyOption
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ServiceSurveysIdQuestionsIdOptionsEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[SurveyOption], ConnectWiseManageRequestParams],
    IPostable[SurveyOption, ConnectWiseManageRequestParams],
    IPaginateable[SurveyOption, ConnectWiseManageRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "options", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[SurveyOption])
        IPostable.__init__(self, SurveyOption)
        IPaginateable.__init__(self, SurveyOption)

        self.count = self._register_child_endpoint(
            ServiceSurveysIdQuestionsIdOptionsCountEndpoint(
                client, parent_endpoint=self
            )
        )

    def id(self, id: int) -> ServiceSurveysIdQuestionsIdOptionsIdEndpoint:
        """
        Sets the ID for this endpoint and returns an initialized ServiceSurveysIdQuestionsIdOptionsIdEndpoint object to move down the chain.

        Parameters:
            id (int): The ID to set.
        Returns:
            ServiceSurveysIdQuestionsIdOptionsIdEndpoint: The initialized ServiceSurveysIdQuestionsIdOptionsIdEndpoint object.
        """
        child = ServiceSurveysIdQuestionsIdOptionsIdEndpoint(
            self.client, parent_endpoint=self
        )
        child._id = id
        return child

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> PaginatedResponse[SurveyOption]:
        """
        Performs a GET request against the /service/surveys/{id}/questions/{id}/options endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[SurveyOption]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            SurveyOption,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> list[SurveyOption]:
        """
        Performs a GET request against the /service/surveys/{id}/questions/{id}/options endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[SurveyOption]: The parsed response data.
        """
        return self._parse_many(
            SurveyOption, super()._make_request("GET", data=data, params=params).json()
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> SurveyOption:
        """
        Performs a POST request against the /service/surveys/{id}/questions/{id}/options endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            SurveyOption: The parsed response data.
        """
        return self._parse_one(
            SurveyOption, super()._make_request("POST", data=data, params=params).json()
        )
