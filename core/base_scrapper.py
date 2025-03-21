import time
import requests

from bs4 import BeautifulSoup

from utils.constants import HEADERS


class BaseScrapper:
    def __init__(self):
        self.parser = {}

    def extract_urls(self):
        return []

    def get_soup(self, url):
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            print(f"Error al acceder a {url}")
            return None
        return BeautifulSoup(response.text, "html.parser")

    def extract_data(self, urls):
        projects_data = []

        for i, url in enumerate(urls):
            # Debug limiter.
            if i == 1:
                break
            print(f"Extracting url: '{url}'")
            soup = self.get_soup(url)
            if not soup:
                continue

            project_info = {}
            for key, locator in self.parser.items():
                element = soup.select_one(locator["selector"])
                if element:
                    text = element.get_text(strip=True)
                    if locator["parser"]:
                        text = locator["parser"](text)
                    project_info[key] = text
                else:
                    project_info[key] = None

            projects_data.append(project_info)
            time.sleep(0.25)

        return projects_data

    def get_projects_data(self):
        project_urls = self.extract_urls()
        projects_data = self.extract_data(project_urls)
        return projects_data
