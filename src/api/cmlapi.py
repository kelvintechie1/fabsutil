"""Module to interact with Cisco Modeling Labs 2.0 API"""
# Import libraries
from .apiobject import API

class CMLAPI(API):
    """Object for interacting with CML API"""
    def __init__(self, lab_id, **kwargs):
        self.lab_id = lab_id
        super().__init__(**kwargs)

    def authAPI(self):
        """Authenticate to CML API and obtain Bearer Token for Authorization Header"""
        body = {"username": self.username, "password": self.password}
        authToAPI = self.post(url='/authenticate', json=body)
        self.headers["Authorization"] = "Bearer " + authToAPI.text.strip('"')

    def buildDevicesList(self):
        """Query CML lab for list of all devices and selected attributes: 
        device ID, device name, device type"""
        nodes = [{"id": device["id"], "name": device["label"], "nodeType":
                  device["node_definition"]} for device in
                  self.get(url=f"/labs/{self.lab_id}/nodes", params={"data": "true"}).json()]

        return nodes

    def buildLinksList(self):
        """Query CML lab for list of all links in the lab connecting lab devices"""
        links = [{"id": link["id"], "name": link["label"],
                  "interface_a": link["interface_a"], "interface_b": link["interface_b"],
                  "node_a": link["node_a"], "node_b": link["node_b"], "state": link["state"]}
                  for link in self.get(url=f"/labs/{self.lab_id}/links",
                                       params={"data": "true"}).json()]

        return links

    def buildPortsList(self, node_id):
        """Query CML lab for list of all connected ports on a given device"""
        ports = [{"id": port["id"], "name": port["label"], "mac_address": port["mac_address"],
                       "connected": port["is_connected"],
                       "state": port["state"]} 
                       for port in self.get(url=f"/labs/{self.lab_id}/nodes/{node_id}/interfaces",
                                            params={"data": "true"}).json()]

        return ports

    def assignConsoleTelnetPort(self, node_id, portNum):
        """Use CML2's PATty to assign port numbers to each device"""
        portTag = [f"serial:{portNum}"]
        existingTags = self.get(url=f"/labs/{self.lab_id}/nodes/{node_id}",
                                params={"data": "true"}).json()["tags"]
        if portTag not in existingTags:
            newTags = {"tags": existingTags + portTag}
            self.patch(url=f"/labs/{self.lab_id}/nodes/{node_id}", json=newTags)
