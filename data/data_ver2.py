import psycopg2
import requests
from bs4 import BeautifulSoup
# conn = psycopg2.connect(
#     host="localhost",
#     database="Sdata",
#     user="postgres",
#     password="eba.1117"
# )
# cur = conn.cursor()
# cur.execute("SELECT * FROM mytable")
# rows = cur.fetchall()
# for row in rows:
#     print(row)
# conn.close()
inp = ['https://www.unegui.mn/adv/6879778_subaru-xt-2012-2012/']
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
    print(data,'\n',data1,'\n',data2_dict)