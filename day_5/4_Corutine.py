import asyncio
import time

async def print_mesaj(mesaj, nr_itearatii):
    for i in range(nr_itearatii):
        await asyncio.sleep(2)
        print(mesaj)

async def functie_blocanta():
    contor = 1
    while True:
        await print_mesaj('Salut din functia blocanta', 1)

        time.sleep(3)
        print('Inca procesez')
        contor += 1
        if contor==5:
            break


event_loop = asyncio.get_event_loop()
#t2 = event_loop.create_task(print_mesaj("Salut ! Sunt task-ul 2",3))
#t1 = event_loop.create_task(print_mesaj("Salut ! Sunt task-ul 1",2))

tasks = [print_mesaj("Salut ! Sunt task-ul {}".format(i),i) for i in range(5)]

t3 = event_loop.create_task(functie_blocanta())


event_loop.run_until_complete(asyncio.gather(*tasks, t3))


event_loop.close()