# Import libraries
import requests as rq
from getpass import getpass
from json import dumps

# Device Class - Device in topology
class Device:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.links = {}
    def addLink(self, otherNode):
        pass

def createAuthedAPIObject(apiURL, username, password):
    class API(rq.Session):
        def __init__(self, baseURL, username, password, *args, **kwargs):
            self.baseURL = baseURL
            self.username = username
            self.password = password
            super().__init__(*args, **kwargs)
        def authAPI(self):
            body = {"username": username, "password": password}
            authToAPI = self.post(url=self.baseURL, json=body)
            if authToAPI.status_code == 200:
                self.headers["Authorization"] = "Bearer " + authToAPI.text.strip('"')
                return None
            else:
                return authToAPI.status_code

    session = API(apiURL, username, password)
    if True: # CHANGE THIS TO ADD PARAM LATER
        session.verify = False
        import urllib3
        urllib3.disable_warnings()
    session.authAPI()

    print(session.headers["Authorization"])

    return session

# Testing only - remove later
if __name__ == "__main__":
    createAuthedAPIObject("https://ktl-csco-cml01.lab.trankelvin.com/api/v0/authenticate", 
                          input("Enter your username: "), getpass("Enter your password: "))

