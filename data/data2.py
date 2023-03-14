import psycopg2
import requests
from bs4 import BeautifulSoup
import xlsxwriter

inp = ['https://www.unegui.mn/adv/6879778_subaru-xt-2012-2012/',
       'https://www.unegui.mn/adv/6948378_toyota-prius-30-2013-2023/']
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
    keys = list(data2_dict.keys())
    urt = len(keys)

    workbook = xlsxwriter.Workbook("uneguis-automashin.xlsx")
    worksheet = workbook.add_worksheet("firstSheet")

    for i in range(0, urt):
        worksheet.write(0,i,keys[i])    
    for i,entry in enumerate(data2_dict):
        worksheet.write(1, i,data2_dict[keys[i]])
        
    print(data,'\n',data1,'\n',data2_dict,'\n',keys)
    workbook.close()