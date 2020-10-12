# this is a vey basic calculator

print("Welcome to my calculator in Python. You have the following choices: ")
print("1. Addition\n2. Subtraction\n3.Multiplication\n4.Division\n")
print("So what do you want to do?")

choice = input()
choice = int(choice)

num_one = input("Enter the first number: ")
num_two = input("Enter the second number: ")

num_one = float(num_one)
num_two = float(num_two)

if choice == 1:
    print(num_one + num_two)
elif choice == 2:
    print(num_one - num_two)
elif choice == 3:
    print(num_one * num_two)
elif choice == 4:
    print(num_one / num_two)