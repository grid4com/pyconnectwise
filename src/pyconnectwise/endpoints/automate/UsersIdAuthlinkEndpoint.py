from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IPostable,
)
from pyconnectwise.models.automate import LabTechAuthServiceCredentials
from pyconnectwise.types import (
    JSON,
    ConnectWiseAutomateRequestParams,
)


class UsersIdAuthlinkEndpoint(
    ConnectWiseEndpoint,
    IPostable[LabTechAuthServiceCredentials, ConnectWiseAutomateRequestParams],
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Authlink", parent_endpoint=parent_endpoint
        )
        IPostable.__init__(self, LabTechAuthServiceCredentials)

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseAutomateRequestParams | None = None,
    ) -> LabTechAuthServiceCredentials:
        """
        Performs a POST request against the /Users/{id}/Authlink endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            LabTechAuthServiceCredentials: The parsed response data.
        """
        return self._parse_one(
            LabTechAuthServiceCredentials,
            super()._make_request("POST", data=data, params=params).json(),
        )
