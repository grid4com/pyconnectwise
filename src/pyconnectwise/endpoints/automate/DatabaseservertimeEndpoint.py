from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class DatabaseservertimeEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Databaseservertime", parent_endpoint=parent_endpoint
        )
