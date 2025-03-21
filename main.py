import json
from scrappers.project.project_scrapper import ProjectScrapper


project_scrapper = ProjectScrapper()
projects_data = project_scrapper.get_projects_data()

with open("projects_data.json", "w", encoding="utf-8") as json_file:
    json.dump(projects_data, json_file, ensure_ascii=False, indent=4)
