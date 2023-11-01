from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IGettable,
    IPaginateable,
    IPostable,
)
from pyconnectwise.models.automate import LabTechTemplateAvailableProperty
from pyconnectwise.responses.paginated_response import PaginatedResponse
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class TemplateavailablepropertiesEndpoint(
    ConnectWiseEndpoint,
    IGettable[list[LabTechTemplateAvailableProperty], ConnectWiseAutomateRequestParams],
    IPostable[LabTechTemplateAvailableProperty, ConnectWiseAutomateRequestParams],
    IPaginateable[LabTechTemplateAvailableProperty, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Templateavailableproperties", parent_endpoint=parent_endpoint
        )
        IGettable.__init__(self, list[LabTechTemplateAvailableProperty])
        IPostable.__init__(self, LabTechTemplateAvailableProperty)
        IPaginateable.__init__(self, LabTechTemplateAvailableProperty)

    def paginated(
        self,
        page: int,
        page_size: int,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> PaginatedResponse[LabTechTemplateAvailableProperty]:
        """
        Performs a GET request against the /Templateavailableproperties endpoint and returns an initialized PaginatedResponse object.

        Parameters:
            page (int): The page number to request.
            page_size (int): The number of results to return per page.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            PaginatedResponse[LabTechTemplateAvailableProperty]: The initialized PaginatedResponse object.
        """
        if params:
            params["page"] = page
            params["pageSize"] = page_size
        else:
            params = {"page": page, "pageSize": page_size}
        return PaginatedResponse(
            super()._make_request("GET", params=params),
            LabTechTemplateAvailableProperty,
            self,
            page,
            page_size,
            params,
        )

    def get(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> list[LabTechTemplateAvailableProperty]:
        """
        Performs a GET request against the /Templateavailableproperties endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            list[LabTechTemplateAvailableProperty]: The parsed response data.
        """
        return self._parse_many(
            LabTechTemplateAvailableProperty,
            super()._make_request("GET", data=data, params=params).json(),
        )

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> LabTechTemplateAvailableProperty:
        """
        Performs a POST request against the /Templateavailableproperties endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechTemplateAvailableProperty: The parsed response data.
        """
        return self._parse_one(
            LabTechTemplateAvailableProperty,
            super()._make_request("POST", data=data, params=params).json(),
        )
