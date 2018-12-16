import json
import aiohttp
import asyncio

async def get_meteo_data(json_data):
    parser = json_data
    prognoza_zilei = []
    for prognoza in parser['weather']:
        prognoza_zilei.append(prognoza['description'])
    temperatura = parser['main']['temp']
    locatie = parser['name']

    print('Locatie {} - temperatura: {}'.format(locatie,temperatura))
    for evenimente in prognoza_zilei:
        print(evenimente)

async def get_json_meteo(url):
    async with aiohttp.ClientSession() as session:
        #await asyncio.sleep(10)
        continut = await session.get(url)
        #print(await continut.json())
        continut_json = await continut.json()
        await get_meteo_data(continut_json)

async def print_loading():
    for i in range (0,5):
        await asyncio.sleep(1)
        print("Loading data...")

url = "http://api.openweathermap.org/data/2.5/weather?q=Bucharest&appid=7b10426ee90376dc3d6525f847128b35&units=metric&format=json&lang=ro"

event_loop = asyncio.get_event_loop()
task_load = event_loop.create_task(get_json_meteo(url))
task_mesaj = event_loop.create_task(print_loading())

terminate, active = event_loop.run_until_complete(asyncio.wait([task_load,task_mesaj], return_when=asyncio.FIRST_COMPLETED))
for task in terminate:
    #print("Task terminat")
    if(task._coro.__name__ == 'get_json_meteo'):
        for active_task in active:
            active_task.cancel()
        event_loop.run_until_complete(asyncio.wait(active))
    if(task._coro.__name__ == 'print_loading'):
        print("Imposibil de descarcat json")
        for active_task in active:
            active_task.cancel()
        event_loop.run_until_complete(asyncio.wait(active))


event_loop.close()

print('Done')