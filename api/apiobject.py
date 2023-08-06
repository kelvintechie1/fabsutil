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