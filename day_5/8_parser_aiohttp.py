import aiohttp
import asyncio
from bs4 import BeautifulSoup

async def get_continut_pagina(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            #print(resp.status)
            #print(await resp.text())
            continut = await resp.text()
            await get_curs_valutar(continut)

async def get_curs_valutar(continut_pagina):
    soup = BeautifulSoup(continut_pagina, features="html.parser")
    divs = soup.find_all('div', attrs={'class':'currency-value'})
    for div in divs:
        div_cotatie = div.select('div.value')
        if(len(div_cotatie) > 0 and div_cotatie[0].get_text().find('EURO')!=-1 \
        and div_cotatie[0].get_text().find('USD')==-1):
            print(div_cotatie[0].get_text().split(' ')[3])

event_loop = asyncio.get_event_loop()

url = 'https://www.cursbnr.ro/'
task1 = event_loop.create_task(get_continut_pagina(url))

event_loop.run_until_complete(asyncio.gather(task1))

event_loop.close()