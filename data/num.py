import requests
from bs4 import BeautifulSoup

# Make a GET request to the website
inp = ['https://www.unegui.mn/adv/6690393_nissan-patrol-2022-2022/',
       'https://www.unegui.mn/adv/6952318_hyundai-sonata-2010-2015/']
l = len(inp)
for i in range(0,l):
    # Parse the HTML content using BeautifulSoup
    url = inp[i]
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    number = soup.find('span',class_="number-announcement").text.split(':')
    number = [line.strip() for line in number if line.strip()]
    number_dict = {}
    for i in range(0, len(number), 2):
        number_dict[number[i]] = number[i+1]
    print(number_dict)