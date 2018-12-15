from bs4 import BeautifulSoup
import requests

class lego:

    def __init__(self):
        self.id = 0
        self.name = ''
        self.prices = []
        self.collection = ''



def get_collection_sets(list):
    for div_id in list:
        #get collection name
        collection = ''
        header = div_id.select('h2')
        if (len(header)!=0):
            collection = header[0].get_text().replace('Hide','')
    
        rows = div_id.findAll('tr', attrs={'class':'notwanted'})

        for row in rows:

            lego_set = lego()
            lego_set.collection = collection

            #print(row.encode("utf-8").prettify())
            #get header
            header = row.select('div h1')
            if(len(header)!=0):
                lego_set.name = row.select('div h1')[0].get_text()
        
            #get id
            links = row.select('td a.highslide')
            for link in links:
                lego_set.id = link.get_text()

            # get prices
            tds = row.findAll('td', attrs={'class':'textright'})
        
            for td in tds:
                price = td.select('span a')
                if(len(price) > 0):
                    price_value = price[0].get_text()
                    lego_set.prices.append(float(price_value.replace('L','')))
                    #print(price_value)

            print(lego_set.__dict__)


url = "https://brickset.com/buy/amazon"
#result = requests.get(url)
#c = result.content

#priceFile = open("prices.html","w", encoding='utf-8')
#priceFile.write(c.decode("utf-8") )
#priceFile.close()

#soup = BeautifulSoup(c, "html.parser")

f = open('prices.html', encoding='utf-8')
soup = BeautifulSoup(f.read(), "html.parser") 
f.close()


ids_list = soup.find_all('div', attrs={'class':'amazonlist amazonblock'})
for id in ids_list:
    print(id['id'])
    list = soup.findAll('div', attrs={'id':id['id']})
    get_collection_sets(list)
    
