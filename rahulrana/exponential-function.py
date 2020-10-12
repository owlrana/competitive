# to raise a number to some exponential 

# to get 2 to the power 3
print(2**3)

# but let us use for loop to do this

def raise_the_num(base_number, raise_number):
    result = 1
    for i in range(raise_number):
        result = result * base_number

    return result

base_number = int(input("Please enter the base number you want to raise: "))
raise_number = int(input("Please enter how much you want to raise it: "))

print(raise_the_num(base_number, raise_number))