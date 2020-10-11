# Program to find the factorial of a number

def factorial (n):
    factorial = 1

    for i in range (1, n+1):
        factorial = factorial * i

    return factorial

n = int(input("Please enter a number whose factorial you want to create: "))

print(factorial(n))