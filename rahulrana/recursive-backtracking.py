# to make all combinations of letters in a list through recursion backtracking
# remove '#' to debug, check the flow of my progrma as it's bti weird lol

def nestedFors (n, firstFor, x, countfor, countelse):
    #print('FRESH LIST CONDITION: ', x)
    if firstFor < n:
        #print('ENTER IF: ')
        #iterating and changing the values of the list's indices (using it as variable)
        for x [firstFor] in ['a', 'b']:
            #print('ENTER FOR: ')
            nestedFors (n, firstFor + 1, x, countfor, countelse)
            countfor += 1
            #print('OUT FOR: ', countfor)
        #print('OUT IF: ')
    else:
        #print('ENTER ELSE: ')
        print(x)
        countelse += 1
        #print('OUT ELSE: ', countelse)

# Doesn't matter what is there in the list, we are going to replace with a, bs instead later
x = ['x', 'y', 'z']
countfor = 0
countelse = 0

nestedFors(len(x), 0, x, countfor, countelse)