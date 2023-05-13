#Code to test if we have permission to scrape a website

import requests

from bs4 import BeautifulSoup

url = input("Enter the URL of the website: ")

r = requests.get(url)

print(r.status_code)
    