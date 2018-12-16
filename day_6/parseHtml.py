import requests
from bs4 import BeautifulSoup

def getUrl(url):
    page = requests.get(url)
    content  = page.content
    return content

page = getUrl('http://google.ro')

soup = BeautifulSoup(page, features='html.parser')
links = soup.find_all('a')

for link in links:
    name = link.text
    href = link.attrs['href']
    print(name, href)

html_file = open('C:\\Users\\bogda\\Desktop\\Python\\PythonExamples\\day_6\\sample_files\\sample_page.html')

soup = BeautifulSoup(html_file, features='html.parser')

print(soup.title.string)

html_file.close()
