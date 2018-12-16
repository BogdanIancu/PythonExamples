import xml.etree.ElementTree

#incarcam fisierul xml
parser_xml = xml.etree.ElementTree.parse('date.xml')
#get GDP for Singapore
root  = parser_xml.getroot()
for country in root:
    if(country.get('name') == 'Singapore'):
        print("GDP for Singapore = {}".format(country[2].text))
