import requests
from bs4 import BeautifulSoup
import xlsxwriter

main_data = []

inp = ['https://www.unegui.mn/adv/6879778_subaru-xt-2012-2012/',
       'https://www.unegui.mn/adv/6948378_toyota-prius-30-2013-2023/',
       'https://www.unegui.mn/adv/6996937_bmw-3-seri-2002-2012/']
l = len(inp)
for i in range(0,l):
    url = inp[i]
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')

    data = soup.find('ul',class_='breadcrumbs').text.split('\n') # get breadcrumbs
    data = [element for element in data if element != ''][1]

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

    keys = list(dicts.keys())
    urt = len(keys)
    main_data.append(dicts)

    workbook = xlsxwriter.Workbook("unegui_mn.xlsx")
    worksheet = workbook.add_worksheet("firstSheet")

    for i in range(0, urt):
        worksheet.write(0,i,keys[i])    
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
print(main_data)
    