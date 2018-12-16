import xml.etree.ElementTree as ET

xml_obj = ET.parse('C:\\Users\\bogda\\Desktop\\Python\\PythonExamples\\day_6\\sample_files\\note.xml')

root = xml_obj.getroot()
print(root.tag)

for childNode in root:
    print(childNode.tag, childNode.attrib.get('name'))

print(root[0][1].text)
for n in root[2].findall('neighbor'):
    print(n.get('name'))