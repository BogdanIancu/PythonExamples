import aiohttp
import requests
from bs4 import BeautifulSoup

url = 'https://www.cursbnr.ro/'

#descarcam pagina local sync
pagina = requests.get(url)
continut = pagina.text()

soup = BeautifulSoup(continut, features="html.parser")
#print(soup.prettify())


#extrag div-urile cu clasa currency-value
divs = soup.find_all('div', attrs={'class':'currency-value'})

# print(divs)
#extrag valoare EURO
for div in divs:
    #print(div.get_text())
    #extrag div-ul cu clasa value
    div_cotatie = div.select('div.value')
    #print(div_cotatie)
    if(len(div_cotatie) > 0 and div_cotatie[0].get_text().find('EURO')!=-1 \
     and div_cotatie[0].get_text().find('USD')==-1):
        print(div_cotatie[0].get_text().split(' ')[3])



