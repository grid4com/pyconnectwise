from pyconnectwise.endpoints.base.connectwise_endpoint import ConnectWiseEndpoint


class ApprovalpoliciesEndpoint(ConnectWiseEndpoint):
    def __init__(self, client, parent_endpoint=None):
        ConnectWiseEndpoint.__init__(
            self, client, "Approvalpolicies", parent_endpoint=parent_endpoint
        )
