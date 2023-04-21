import requests
from bs4 import BeautifulSoup

i = 200
while i > 0:
    url = "https://www.unegui.mn/avto-mashin/-avtomashin-zarna/?page=" + str(i)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all('a',{"class": "announcement-block__title"})
    link_urls = [link.get("href") for link in links]
    for urls in link_urls:
        urls = "https://www.unegui.mn" + str(urls)
        with open('urls.txt', 'a') as f:
            f.write(str(urls))
            f.write("\n")
    i = i - 1