#to find the sum of 1/(n.n+1) from n = 1 to n = 99

def findsum(n):
    sum = 0.0000
    for num in range(1, n):
        sum = sum + 1/( num ) * ( num+1 )

    return sum

n = int(input('Please enter the value of n: '))
print(findsum(n))