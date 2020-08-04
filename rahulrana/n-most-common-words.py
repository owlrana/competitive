#we can easily find the most common word by just a variable, but this is how one might find a SET of most common words

#ask for the name of the file
fname = input('Please enter the name of the file you want to find the 10 most common words from')
if fname == '':
    fname = 'romeo.txt'
fhandle = open(fname)

#now keep track of the words in a dictionary
counts_dict = dict()
for lines in fhandle:
    words = lines.split()
    for word in words:
        counts_dict[word] = counts_dict.get(word, 0) + 1

#now create a list with reverse keys and values to sort and print by key
tmp_list = list()
for (key, value) in counts_dict.items():
    tmp_list.append( (value, key) ) #exchanged the order

#now sort the list of tuples
tmp_list = sorted(tmp_list, reverse = True) #as we need keys in decreasing order

#now print from 0 to 10 (not including 10)
for (value, key) in tmp_list[:10]: #tmp_list means all, [0:10] means 0 to 10
    print(key, value) #reversed the order again as the key/values were exchanged