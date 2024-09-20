"""API Access Errors"""
class APIError(Exception):
    """Raise error specifying details for HTTP/REST API access errors"""
    def __init__(self, status, reason, url):
        super().__init__(f"Error {status}: {reason}, URL: {url}")
