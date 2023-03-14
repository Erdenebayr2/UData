import requests
from bs4 import BeautifulSoup

# Make a GET request to the website
url = "https://www.unegui.mn/avto-mashin/-avtomashin-zarna"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")
# Find all the links on the website using the "a" tag
links = []
for link in soup.find_all("a"):
    href = link.get("href")
    if href is not None:
        links.append(href)

# Print all the links
for link in links:
    print(link)
