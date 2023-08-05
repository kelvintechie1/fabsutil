# Import libraries
import requests as rq

class API(rq.Session):
    def __init__(self, baseURL, username, password, verifyStatus, *args, **kwargs):
        self.baseURL = baseURL
        self.username = username
        self.password = password
        super().__init__(*args, **kwargs)

        if not verifyStatus:
            self.verify = False
    
    def request(self, method, url, *args, **kwargs):
        return super().request(method, (self.baseURL + url), *args, **kwargs)

    def authAPI(self):
        body = {"username": self.username, "password": self.password}
        authToAPI = self.post(url='/authenticate', json=body)
        if authToAPI.status_code == 200:
            self.headers["Authorization"] = "Bearer " + authToAPI.text.strip('"')
            return None
        else:
            return authToAPI.status_code
    
    def buildDevicesList(self, lab_id="a724ee41-7524-462a-9c53-ea749e4167b2"):
        nodes = [[device["id"], device["label"], device["node_definition"]] for device in 
                 self.get(url=f"/labs/{lab_id}/nodes", params={"data": "true"}).json()]
        
        return nodes