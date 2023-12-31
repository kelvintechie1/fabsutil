# Import libraries
import requests as rq
from .apiobject import API

class CMLAPI(API):
    def authAPI(self):
        body = {"username": self.username, "password": self.password}
        authToAPI = self.post(url='/authenticate', json=body)
        self.headers["Authorization"] = "Bearer " + authToAPI.text.strip('"')
        return None
    
    def buildDevicesList(self, lab_id):
        nodes = [{"id": device["id"], "name": device["label"], "nodeType": device["node_definition"]} 
                 for device in self.get(url=f"/labs/{lab_id}/nodes", params={"data": "true"}).json()]
        
        return nodes
    
    def buildPortsList(self, lab_id, node_id):
        ports = [{"id": port["id"], "name": port["label"], "mac_address": port["mac_address"],
                       "connected": port["is_connected"], "state": port["state"]} 
                       for port in self.get(url=f"/labs/{lab_id}/nodes/{node_id}/interfaces", params={"data": "true"}).json()]
        
        return ports
    
    def buildLinksList(self, lab_id):
        links = [{"id": link["id"], "name": link["label"], 
                  "interface_a": link["interface_a"], "interface_b": link["interface_b"],
                  "node_a": link["node_a"], "node_b": link["node_b"], "state": link["state"]}
                  for link in self.get(url=f"/labs/{lab_id}/links", params={"data": "true"}).json()]
        
        return links
        
            