#this program is to check syntaxes and programs while you learn
words = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

words_list = words.split()
email = words_list[1]

email_list = email.split('@')
host = email_list[1]