#Practice file to check code while taking lectures and notes. Code available for the last lecture and last check only.

purse = dict()
purse['monkey'] = None

value = input('Enter the value you want to store: ')
key = input('Enter the name of the key to access it: ')

if value == 'None':
    value = None
elif value == '':
    value = 'DefaultValue'

if key == '':
    key = 'DefaultKey'

purse[key] = value


print(purse)