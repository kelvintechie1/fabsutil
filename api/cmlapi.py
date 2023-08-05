# Import libraries
import requests as rq
from .apiobject import API

class CMLAPI(API):
    def authAPI(self):
        body = {"username": self.username, "password": self.password}
        authToAPI = self.post(url='/authenticate', json=body)
        if authToAPI.status_code == 200:
            self.headers["Authorization"] = "Bearer " + authToAPI.text.strip('"')
            return None
        else:
            return authToAPI.status_code
    
    def buildDevicesList(self, lab_id):
        nodes = [{"id": device["id"], "name": device["label"], "nodeType": device["node_definition"]} 
                 for device in self.get(url=f"/labs/{lab_id}/nodes", params={"data": "true"}).json()]
        
        return nodes
    
    def buildInterfacesList(self, lab_id, node_id):
        interfaces = [{"id": interface["id"], "name": interface["label"], 
                       "mac_address": interface["mac_address"], "state": interface["state"]} 
                       for interface in self.get(url=f"/labs/{lab_id}/nodes/{node_id}/interfaces", params={"data": "true"})]
        
        return interfaces
    
    def buildLinksList(self, lab_id):
        links = [{"id": link["id"], "name": link["label"], 
                  "interface_a": link["interface_a"], "interface_b": link["interface_b"],
                  "node_a": link["node_a"], "node_b": link["node_b"], "state": link["state"]}
                  for link in self.get(url=f"/labs/{lab_id}/links", params={"data": "true"})]
        
        return links