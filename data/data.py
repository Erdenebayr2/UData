import requests
from bs4 import BeautifulSoup
# unegui.mn eрөнхий бичиглэл

inp = ['https://www.unegui.mn/adv/6879778_subaru-xt-2012-2012/']
l = len(inp)
for i in range(0,l):
    url = inp[i]
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')

    data = soup.find('ul',class_='breadcrumbs').text.split('\n') # get breadcrumbs
    data = [element for element in data if element != '']
    data = data[-3]+'/'+data[-2]+'/'+data[-1]

    data1 = soup.find('h1').text.split('\n') # get title
    data1 = [element for element in data1 if element != '']
    data1 = [line.strip() for line in data1 if line.strip()][0]


    data2 = soup.find('ul',class_='chars-column').text.split('\n') # get values
    data2 = [element for element in data2 if element != '']
    data2 = [line.strip() for line in data2 if line.strip()]
    data2_dict = {}
    for i in range(0, len(data2), 2):
        data2_dict[data2[i]] = data2[i+1]

    date = soup.find('span', class_='date-meta').text[11:-6]
    print(date)
    price = soup.find('meta', {'itemprop': 'price'})['content']

    desc = soup.find('div', class_='js-description').text.split('\n')
    desc = [element for element in desc if element != ''][0]

    data2_dict['Тайлбар'] = desc
    data2_dict['Үнэ'] = price
    dicts = {'Гарчиг':data1,'Огноо':date,'Марк':data}
    dicts.update(data2_dict)
    print(dicts)