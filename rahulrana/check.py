#Practice file to check code while taking lectures and notes. Code available for the last lecture and last check only.

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