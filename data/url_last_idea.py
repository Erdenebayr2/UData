import requests
from bs4 import BeautifulSoup

url = 'https://www.unegui.mn/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

for link in soup.find_all('a'):
    link_url = link.get('href')
    link_url = url[:21]+link_url
    if link_url is not None:
        link_response = requests.get(link_url)
        link_soup = BeautifulSoup(link_response.content, 'html.parser')
        print(link_soup.get_text())
