from typing import Any

from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint
from pyconnectwise.endpoints.manage.ScheduleHolidaylistsIdHolidaysEndpoint import ScheduleHolidaylistsIdHolidaysEndpoint
from pyconnectwise.endpoints.manage.ScheduleHolidaylistsIdInfoEndpoint import ScheduleHolidaylistsIdInfoEndpoint
from pyconnectwise.models.base.message_model import GenericMessageModel
from pyconnectwise.responses.paginated_response import PaginatedResponse


class ScheduleHolidaylistsIdEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        super().__init__(client, "{id}", parent_endpoint=parent_endpoint)

        self.info = self._register_child_endpoint(ScheduleHolidaylistsIdInfoEndpoint(client, parent_endpoint=self))
        self.holidays = self._register_child_endpoint(
            ScheduleHolidaylistsIdHolidaysEndpoint(client, parent_endpoint=self)
        )