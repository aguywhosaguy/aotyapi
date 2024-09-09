from cloudscraper import CloudScraper
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from aotyapi import constants

BASEURL = "https://www.albumoftheyear.org/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537."
}

class AOTYClient(CloudScraper):
    """
        Client for using AOTY.
        Inherits CloudScraper and Session for bypassing CloudFlare restrictions.
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.baseURL = BASEURL

    def request(self, method: str, url: str, *args, **kwargs):
        return super().request(method, urljoin(self.baseURL, url), *args, **kwargs)

    def critic_year_list(self, year: int, source: constants.Critic = 0, min_reviews: int = 5, page: int = 1):
        link = f"ratings/{source}-highest-rated/{year}/{page}?r={min_reviews}"
        return link

    def get_critic(self, num: int):
        resp = self.request("get", f"ratings/{num}-highest-rated/all/1")
        soup = BeautifulSoup(resp.text, "html.parser")
        pubhead = soup.find("div", {"class": "publicationHeader"})
        if pubhead:
            publisher = pubhead.h1.string
            return publisher
        return None
