import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

# example of website url to use

url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url)
"""
html_bytes = page.read()  # this extracts the html from the page
html = html_bytes.decode("utf-8")  # this decoded the bytes into string for reading
"""
# or you can use just one statement
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")


