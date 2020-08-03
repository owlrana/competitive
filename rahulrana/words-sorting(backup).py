#Battery running low so this is the backup of last working code

fname = input("Enter file name: ")
fhandle = open(fname)

lst = list()
words_list = list()
flag = False

for line in fhandle:
    lst = (line.split())
    for realwords in lst:
        for storedwords in words_list:
            if storedwords == realwords:
                flag = True
        if flag == False:
            words_list.append(realwords)
		elif flag == True:
            continue
            
print(words_list)