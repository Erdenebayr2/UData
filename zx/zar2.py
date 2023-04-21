from bs4 import BeautifulSoup
import httpx
import asyncio

async def main2():
    url = 'https://www.unegui.mn/utas--dugaar/uhaalag-tsag-smart-watch/?page='
    x = []
    async with httpx.AsyncClient() as client:
        reqs = [client.get(url + str(i)) for i in range(1, 11)]
        responses = await asyncio.gather(*reqs)
    soups = [BeautifulSoup(response.content, 'html.parser') for response in responses]

    numbers = [soup.find('ul', class_='number-list').text.split('\n')[-2] if soup.find('ul', class_='number-list') else '1' for soup in soups]
    ulist = set()
    for number in numbers:
        urls = url + str(number)
        async with httpx.AsyncClient() as client:
            response = await client.get(urls)
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a', {"class": "announcement-block__title"})
        link_urls = ["https://www.unegui.mn" + link.get('href') for link in links]
        ulist.update(link_urls)
    print(len(ulist))
    return list(ulist)

asyncio.run(main2())

