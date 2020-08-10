#creating xml data in python and then using a tree to access it 

import xml.etree.ElementTree as ET

data = '''<person>
    <name>Chuck</name>
    <phone type="intl">
        +91 844 791 7137
    </phone>
    <email hide="nope"/>
</person>'''

tree = ET.fromstring(data) #creates a tree and stores all the values in that tree so everything is organised
print('Name:', tree.find('name').text) #gives back the child, the text in it
print('Attr:', tree.find('email').get('hide')) #gives back the attribute in it and NOT the text or other stuff