import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# print(page.text) """ this retrieves data directly in html format & structures """
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

jobs_elements = results.find_all("div", class_="card-content")
for job_element in jobs_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    """
    print(title_element.text.strip()) # the strip() is to remove the excess whitespace from the text
    print(company_element.text.strip())
    print(location_element.text.strip())
    print() """

# this using the string argument method to find the specific material you are searching for
# python_jobs = results.find_all("h2", string="python")

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
""" here we are creating an anonymous function in the string argument"""
# print(len(python_jobs))
# print(results.prettify())

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]
for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())  # the strip() is to remove the excess whitespace from the text
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()

    links = job_element.find_all("a")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")


