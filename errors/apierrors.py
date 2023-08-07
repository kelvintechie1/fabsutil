class APIError(Exception):
    def __init__(self, status, reason, url):
        self.message = f"Error {status}: {reason}, URL: {url}"
        super().__init__(self.message)