import requests
from bs4 import BeautifulSoup
url1 = []
url2 = []
url3 = []
url4 = []
url5 = []
url6 = []

site = "https://www.unegui.mn"
slink = "/avto-mashin/-avtomashin-zarna/"
surl = site + slink
response = requests.get(surl)

soup = BeautifulSoup(response.content, "html.parser")
data_url1 = soup.find('ul',class_='rubrics-list clearfix js-toggle-content toggle-content')

for link in data_url1.find_all("a"):
    href = link.get("href")
    if href is not None:
        # if href[0:30] == '/avto-mashin/-avtomashin-zarna':
            url1.append(href)
    # links = list(set(links))

# print(url1) list len 45 items

for i in range(0,len(url1)):
    surl1 = site + url1[i]
    url2.append(surl1)
# print(url2)

#url3
for i in range(0,len(url2)):
    response1 = requests.get(url2[i])
    soup1 = BeautifulSoup(response1.content, "html.parser")
    data_url2 = soup1.find('div',class_='js-toggle toggle-block')
    for link in data_url2.find_all("a"):
        href = link.get("href")
        if href is not None:
            if href == '#':
                pass
            else:
                url3.append(href)
        # links = list(set(links))
    url3 = list(set(url3))
# print(url3)

for i in range(0,len(url3)):
     surl2 = site + url3[i]
     url4.append(surl2)

#url 5

for i in range(0,len(url4)):
    response2 = requests.get(url4[i])
    soup2 = BeautifulSoup(response2.content, "html.parser")
    # data_url3 = soup2.find('div',class_='js-toggle toggle-block')
    for link in soup2.find_all("a"):
        href = link.get("href")
        if href is not None:
            if href == '#':
                pass                
            elif href[13:16] == 'bmw':
                url5.append(href)
        # links = list(set(links))
    url5 = list(set(url5))
print(len(url5))
# for link in url5:
#         print(len(link))
#kajsgdhagsddaksajsd