#automatically uses iteration to input values into a function and store/print the result without the need of any loop

#defined my own function
def myfunc(n):
  return len(n) 

x = map(myfunc, ('apple', 'banana', 'cherry')) #x is now an object, we will convert it into list by list(x), like float() or int() and then print

print(list(x))