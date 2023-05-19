import requests,os
from bs4 import BeautifulSoup
from datetime import date,datetime,timedelta
import xlsxwriter

mlink = "https://www.unegui.mn/l-hdlh/l-hdlh-zarna/?page="
urlss = mlink
print(urlss)
response = requests.get(urlss)
soup = BeautifulSoup(response.content,'html.parser')
number = soup.find('ul',class_='number-list')
if number:
    number = number.text.split('\n')
    number = list(filter(lambda x: x.strip() != '', number))[-1]
else:
    number = '1'
ulist = []
while int(number) > 0:
    urls = urlss + str(number)
    response = requests.get(urls)
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all('a',{"class": "announcement-block__title"})
    link_urls = [link.get("href") for link in links]
    for Ulink in link_urls:
        Ulink = "https://www.unegui.mn" + str(Ulink)
        ulist.append(Ulink)
        ulist = list(set(ulist))
    number = int(number) - 1
    print(ulist)
url = ulist
link = []

for i in range(0,len(url)):
    response = requests.get(url[i])
    soup = BeautifulSoup(response.content,'html.parser')

    mark = soup.find('ul',class_='breadcrumbs').text.split('\n')
    mark = list(filter(lambda x:x.strip() != '',mark))
    mark = mark[-2] + ' / ' +  mark[-1]

    data = soup.find('ul',class_='chars-column').text.split('\n')
    data = list(filter(lambda x: x.strip() != '', data))
    
    if 'Шал:' not in data:
        data[0:2] = ('Шал:','')

    elif 'Тагт:' not in data:
        data[2:4] = ('Тагт:','')

    elif 'Ашиглалтанд орсон он:' not in data:
        data[4:6] = ('Ашиглалтанд орсон он:','')

    elif 'Гараж:' not in data:
        data[6:8] = ('Гараж:','')

    elif 'Цонх:' not in data:
        data[8:10] = ('Цонх:','')

    elif 'Барилгын давхар:' not in data:
        data[10:12] = ('Барилгын давхар:','')

    elif 'Хаалга:' not in data:
        data[12:14] = ('Хаалга:','')

    elif 'Талбай:' not in data:
        data[14:18] = ('Талбай:','')

    elif 'Хэдэн давхарт:' not in data:
        data[18:20] = ('Хэдэн давхарт:','')

    elif 'Лизингээр авах боломж:' not in data:
        data[20:22] = ('Лизингээр авах боломж:','')

    elif 'location:' not in data:
        data[22:24] = ('location:','')

    elif 'Цонхны тоо:' not in data:
        data[24:26] = ('Цонхын тоо:','')

    elif 'Байршил:' not in data:
        data[26:28] = ('Байршил:','')

    elif 'Барилгын явц:' not in data:
        data[28:30] = ('Барилгын явц:', '')

    elif 'Төрөл:' not in data:
        data[30:32] = ('Төрөл:','')

    desc = soup.find('div',class_='js-description').text.split('\n')
    desc = list(filter(lambda x: x.strip() != '', desc))
    desc = ''.join(desc)
    
    prince = soup.find('div',class_='announcement-price__wrapper')
    price = prince.find('meta', {'itemprop': 'price'})['content']

    ogno = soup.find('span', class_='date-meta').text[11:-6]
    unuudr = 'Өнөөдөр'
    uchigdur = 'Өчигдөр'
    yester = datetime.now() - timedelta(days=1)
    yesterday = str(yester.date())
    today = str(date.today())
    if ogno == unuudr:ogno = today
    elif ogno == uchigdur:ogno = yesterday
    else:ogno

    dict = {}
    for i in range(0,len(data), 2):
        if i + 1 < len(data):
            key = data[i].strip(':')
            value = data[i+1]
            dict[key] = value
    
    dict['Тайлбар'] = desc
    dict['Үнэ'] = price
    dicts = {'Марк':mark,'Зарын огноо':ogno}
    dicts.update(dict)
    link.append(dicts)
    print(dicts)

    file_name = mlink[22:-7]
    file_name = file_name.replace("/", "_")
    workbook = xlsxwriter.Workbook(f"{file_name}.xlsx")
    worksheet = workbook.add_worksheet("firstSheet")

    l = list(dicts.keys())
    for i in range(0,len(l)):
        worksheet.write(0,i,l[i])
        for index, entry in enumerate(link):
            worksheet.write(index+1, i, entry[l[i]])
    workbook.close()