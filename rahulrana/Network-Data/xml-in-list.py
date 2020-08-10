# program that shows if we need to find more than one tag how do we find it (stored in a list)

import xml.etree.ElementTree as ET
input = '''<stuff>
    <users>
        <user x='2'>
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x ='7'>
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user') #creates a list of tags, which are in the form of trees themself and have information about thier childs and attributes
print('User count:', len(lst)) 

for item in lst: #looping through the list containing trees
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))