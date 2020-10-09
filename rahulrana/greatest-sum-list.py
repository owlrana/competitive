# To find the greatest sum form the cominations of input of numbers as a list

#function to compute the biggest sum
def greatestSum(a):
    max = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if i != j and a[i] + a[i] > max:
                max = a[i] + a[j]
    return max

i = int(input("Enter values for the variable 1: "))
j = int(input("Enter values for the variable 2: "))
k = int(input("Enter values for the variable 3: "))

a = [i, j, k]

print(greatestSum(a))