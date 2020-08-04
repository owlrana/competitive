#As dictionaries do not give a f about the order, we have other ways to sort them by extracting data as tuples then sorting acc to key or values

d = {'g': 4, 'e':40, 'h': 10, 'a': 9}

#sorted by key
for (k,v) in sorted(d.items()): #d.items() gives a list, which is sorted before looping
    print( (k,v), end = '')

print()

#sorted by value
tmp = list()
for k,v in d.items():
    tmp.append( (v, k) ) #made a temporary copy of tuples of d dictionary data
#sort the temporary list of tuples
tmp = sorted(tmp, reverse = False)
print(tmp)