# If statements in python allow out programs to respond to the input given
# They change the flow of the program so it is not just linear

is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not (is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are tall but not a male")
else:
    print("You are either not male or not tall or not both")


# Comparison operators:

# Function to return the largest of the three numbers

def max_num(num1, num2, num3):
    if num1 >=2 and num1 >= num3:
        return num1
    elif num2 >=1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3,4,5))
    