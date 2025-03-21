import requests

from bs4 import BeautifulSoup
from urllib.parse import urljoin

from scrappers.project.project_parser import PROJECT_PARSER
from core.base_scrapper import BaseScrapper
from utils.constants import HEADERS, BASE_URL


class ProjectScrapper(BaseScrapper):
    def __init__(self):
        self.parser = PROJECT_PARSER

    def extract_urls(self):
        response = requests.get(BASE_URL, headers=HEADERS)
        if response.status_code != 200:
            print("Error al acceder a la página")
            return []

        soup = BeautifulSoup(response.text, "html.parser")
        return [
            urljoin(BASE_URL, link["href"])
            for link in soup.find_all("a", href=True)
            if "idproyecto" in link["href"]
        ]
