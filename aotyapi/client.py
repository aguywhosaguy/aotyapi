from requests import Session
from urllib.parse import urljoin

BASEURL = "https://www.albumoftheyear.org/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537."
}

class AOTYSession(Session):
    """Simple class for sending requests to AOTY"""
    
    def __init__(self):
        super().__init__()
        self.baseURL = BASEURL
        self.headers = HEADERS

    def request(self, method, url, *args, **kwargs):
        return super().request(method, urljoin(self.baseURL, url), *args, **kwargs, headers=self.headers)

