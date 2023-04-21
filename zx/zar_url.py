import requests
from bs4 import BeautifulSoup

url = 'https://www.unegui.mn/kompyuter-busad/notebook/?page='

response = requests.get(url)
soup = BeautifulSoup(response.content,'html.parser')

number = soup.find('ul',class_='number-list')
if number:
    number = number.text.split('\n')
    number = list(filter(lambda x: x.strip() != '', number))[-1]
else:
    number = '1'
ulist = []
while int(number) > 0:
    urls = url + str(number)
    response = requests.get(urls)
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all('a',{"class": "announcement-block__title"})
    link_urls = [link.get("href") for link in links]
    for Ulink in link_urls:
        Ulink = "https://www.unegui.mn" + str(Ulink)
        ulist.append(Ulink)
        ulist = list(set(ulist))
    number = int(number) - 1