import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen


def data_call():
    # the url to open the website
    url = "https://www.century21newhorizon.com/ocean-city-md-vacation-rentals/century-i"
    page_info = requests.get(url)

    soup = BeautifulSoup(page_info.content, "html.parser")
    results = soup.find(class_="section")

    def info():
        co_title = soup.find(class_="title-elements")
        co_info = soup.find(class_="column-2")
        print(co_title.text.strip())
        print("\n")
        print(co_info.text.strip())
    info()

    """" i have failed to get the rest of the property info from the website. try finding a solution from your end."""
    def properties():
        century_properties = results.find_all(
            "h4", string=lambda text: "Century" in text.lower()
        )
        century_property_elements = [
            h4_element.parent for h4_element in century_properties
        ]

        for century_property in century_properties:
            links = century_property.find_all("a")
            for link in links:
                link_url = link["href"]
                print(f"click here: {link_url}\n")
            image = century_property.find("a", class_="image_wrap")
            title = century_property.find("h4", "href")
            print(image)
            print(title)
            print()

    properties()


""" 
listings = results.find_all()
for listing in listings:
title = listing.find("span", id=())"""

data_call()
