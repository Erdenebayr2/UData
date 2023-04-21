import requests
from bs4 import BeautifulSoup
import xlsxwriter
from datetime import date,datetime,timedelta
from zar2 import main2
import httpx,asyncio
from time import perf_counter

async def main():
    ulist = await main2()
    url = ulist
    print(url)
    async with httpx.AsyncClient() as client:
        reqs = [client.get(urls) for urls in url]
        response = await asyncio.gather(*reqs)
    return response
    # url = ulist
    # link = []
    # for i in range(0,len(url)):
        # response = requests.get(url[i])
        
        # soup = BeautifulSoup(response.content,'html.parser')

        # mark = soup.find('ul',class_='breadcrumbs').text.split('\n')
        # mark = list(filter(lambda x:x.strip() != '',mark))
        # mark = mark[-2] + ' / ' +  mark[-1]

        # data = soup.find('ul',class_='chars-column').text.split('\n')
        # data = list(filter(lambda x: x.strip() != '', data))
        # if 'Мотор багтаамж:' in data:
        #     data[1] = data[1][:3]
        #     data[1] = float(data[1])*1000
        #     data[-5] = data[-5][:-4]
        
        # if 'Хаяг байршил:' not in data:
        #     data[2:4] = ('Хаяг байршил:','')

        # desc = soup.find('div',class_='js-description').text.split('\n')
        # desc = list(filter(lambda x: x.strip() != '', desc))
        # desc = ''.join(desc)
        
        # prince = soup.find('div',class_='announcement-price__wrapper')
        # price = prince.find('meta', {'itemprop': 'price'})['content']

        # ogno = soup.find('span', class_='date-meta').text[11:-6]
        # unuudr = 'Өнөөдөр'
        # uchigdur = 'Өчигдөр'
        # yester = datetime.now() - timedelta(days=1)
        # yesterday = str(yester.date())
        # today = str(date.today())
        # if ogno == unuudr:ogno = today
        # elif ogno == uchigdur:ogno = yesterday
        # else:ogno

        # dict = {}
        # for i in range(0,len(data), 2):
        #     key = data[i].strip(':')
        #     value = data[i+1]
        #     dict[key] = value
        
        # dict['Тайлбар'] = desc
        # dict['Үнэ'] = price
        # dicts = {'Марк':mark,'Зарын огноо':ogno}
        # dicts.update(dict)
        # link.append(dicts)

        # workbook = xlsxwriter.Workbook("u.xlsx")
        # worksheet = workbook.add_worksheet("firstSheet")

        # l = list(dicts.keys())
        # for i in range(0,len(l)):
        #     worksheet.write(0,i,l[i])
        #     for index, entry in enumerate(link):
        #         worksheet.write(index+1, i, entry[l[i]])
        # workbook.close()

t1_start = perf_counter()
wtf = asyncio.run(main())
t1_stop = perf_counter()

print("program in seconds:", t1_stop-t1_start)
print(wtf)

