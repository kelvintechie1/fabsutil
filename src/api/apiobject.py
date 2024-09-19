import requests as rq
from errors.apierrors import APIError

class API(rq.Session):
    def __init__(self, baseURL, username, password, verifyStatus, *args, **kwargs):
        self.baseURL = baseURL
        self.username = username
        self.password = password
        super().__init__(*args, **kwargs)

        if not verifyStatus:
            self.verify = False

    def request(self, method, url, *args, **kwargs):
        response = super().request(method, (self.baseURL + url), *args, **kwargs)
        if response.status_code >= 200 and response.status_code <= 299:
            return response
        else:
            raise APIError(response.status_code, response.reason, url)