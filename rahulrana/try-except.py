# try except blocks
# you can specify and get information about the error that happened
# and also you can store that error in a variable to know 
# do not be too broad, always specify error types
try:
    #answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as ZeroError :
    print(ZeroError)
except ValueError:
    print("Invalid Input")