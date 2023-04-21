import requests
from bs4 import BeautifulSoup

url = 'https://www.unegui.mn'

response = requests.get(url)
soup = BeautifulSoup(response.content,'html.parser')

subs = soup.find('div',class_='categories')

for link in subs.find_all("a"):
    href = link.get("href")
    href = url+href+'?page='
    print(href)