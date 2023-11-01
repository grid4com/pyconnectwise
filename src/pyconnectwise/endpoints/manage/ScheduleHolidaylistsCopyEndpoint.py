from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.interfaces import (
    IPostable,
)
from pyconnectwise.models.manage import HolidayList
from pyconnectwise.types import (
    JSON,
    ConnectWiseManageRequestParams,
)


class ScheduleHolidaylistsCopyEndpoint(
    ConnectWiseEndpoint, IPostable[HolidayList, ConnectWiseManageRequestParams]
):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "copy", parent_endpoint=parent_endpoint
        )
        IPostable.__init__(self, HolidayList)

    def post(
        self,
        data: JSON | None = None,
        params: ConnectWiseManageRequestParams | None = None,
    ) -> HolidayList:
        """
        Performs a POST request against the /schedule/holidayLists/copy endpoint.

        Parameters:
            data (dict[str, Any]): The data to send in the request body.
            params (dict[str, int | str]): The parameters to send in the request query string.
        Returns:
            HolidayList: The parsed response data.
        """
        return self._parse_one(
            HolidayList, super()._make_request("POST", data=data, params=params).json()
        )
