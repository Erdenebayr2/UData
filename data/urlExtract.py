import requests
from bs4 import BeautifulSoup
import xlsxwriter
from datetime import date,datetime,timedelta
l_url = []
for i in range(177):
    url = "https://www.unegui.mn/avto-mashin/-avtomashin-zarna/?page=" + str(i)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all("a")
    link_urls = [link.get("href") for link in links]
    for urls in link_urls:
        if urls[:5] == "/adv/":
            urls = "https://www.unegui.mn" + str(urls)
            l_url.append(urls)
            l_url = list(set(l_url))
            
            # with open('urluud.txt', 'a') as f:
            #     f.write(l_url)
            #     f.write("\n")
    # for urlu in l_url:
    #     print(urlu)
print(len(l_url))
main_data = []
inp = l_url
l = len(inp)
for i in range(0,l):
    url = inp[i]
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')

    data = soup.find('ul',class_='breadcrumbs').text.split('\n') # get breadcrumbs
    data = [element for element in data if element != '']
    data = data[-2]+'/'+data[-1]

    data1 = soup.find('h1').text.split('\n') # get title
    data1 = [element for element in data1 if element != '']
    data1 = [line.strip() for line in data1 if line.strip()][0].split(',')[0]

    data2 = soup.find('ul',class_='chars-column') # get values
    if data2:
        data2 = data2.text.split('\n')
    else:
        pass
    if data2 is not None:
        data2 = [element for element in data2 if element != '']
        data2 = [line.strip() for line in data2 if line.strip()]
        data2[1] = data2[1][:3]
        data2[1] = float(data2[1])*1000
        data2[1] = str(data2[1])
        data2[-5] = data2[-5][:-4]
    else:
        pass
    if 'Хаяг байршил:' not in data2:
        data2[10:12] = ('Хаяг байршил:', '')
    else:
        pass
    if 'Үйлдвэрлэсэн он:' not in data2:
        data2[10:12] = ('Үйлдвэрлэсэн он:', '')
    else:
        pass
    data2_dict = {}

    for i in range(0, len(data2), 2):
        data2_dict[data2[i]] = data2[i+1]

    ogno = soup.find('span', class_='date-meta').text[11:-6]
    unuudr = 'Өнөөдөр'
    uchigdur = 'Өчигдөр'
    yester = datetime.now() - timedelta(days=1)
    yesterday = str(yester.date())
    today = str(date.today())

    if ogno == unuudr:
        ogno = today

    elif ogno == uchigdur:
        ogno = yesterday
    
    else:
        ogno

    price = soup.find('meta', {'itemprop': 'price'})['content']

    desc = soup.find('div', class_='js-description').text.split('\n')
    desc = [element for element in desc if element != ''][0]

    data2_dict['Тайлбар'] = desc
    data2_dict['Үнэ'] = price
    dicts = {'Гарчиг':data1,'Огноо':ogno,'Марк':data}
    dicts.update(data2_dict)
    main_data.append(dicts)

    workbook = xlsxwriter.Workbook("unegui_auto.xlsx")
    worksheet = workbook.add_worksheet("firstSheet")

    col = ['Гарчиг','Огноо','Марк','Мотор багтаамж:','Хурдны хайрцаг:','Хүрд:',
     'Төрөл:','Өнгө:','Үйлдвэрлэсэн он:','Орж ирсэн он:','Хөдөлгүүр:',
     'Дотор өнгө:','Лизинг:','Хаяг байршил:','Хөтлөгч:','Явсан:','Нөхцөл:',
     'Хаалга:','Тайлбар','Үнэ']
    lcol = len(col)
    for i in range(0, lcol):
        worksheet.write(0,i,col[i])

    for index,entry in enumerate(main_data):
        worksheet.write(index+1, 0,entry['Гарчиг'])
        worksheet.write(index+1, 1,entry['Огноо'])
        worksheet.write(index+1, 2,entry['Марк'])
        worksheet.write(index+1, 3,entry['Мотор багтаамж:'])
        worksheet.write(index+1, 4,entry['Хурдны хайрцаг:'])
        worksheet.write(index+1, 5,entry['Хүрд:'])
        worksheet.write(index+1, 6,entry['Төрөл:'])
        worksheet.write(index+1, 7,entry['Өнгө:'])
        worksheet.write(index+1, 8,entry['Үйлдвэрлэсэн он:'])
        worksheet.write(index+1, 9,entry['Орж ирсэн он:'])
        worksheet.write(index+1, 10,entry['Хөдөлгүүр:'])
        worksheet.write(index+1, 11,entry['Дотор өнгө:'])
        worksheet.write(index+1, 12,entry['Лизинг:'])
        worksheet.write(index+1, 13,entry['Хаяг байршил:'])
        worksheet.write(index+1, 14,entry['Хөтлөгч:'])
        worksheet.write(index+1, 15,entry['Явсан:'])
        worksheet.write(index+1, 16,entry['Нөхцөл:'])
        worksheet.write(index+1, 17,entry['Хаалга:'])
        worksheet.write(index+1, 18,entry['Тайлбар'])
        worksheet.write(index+1, 19,entry['Үнэ'])
    workbook.close()