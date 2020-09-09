# To find an example by inputting the value on n by hand and see if the number is prime or not

n = int(input('Enter the value of n you want to chek for: '))

num = n * n + n + 41

def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             

print(test_prime(num))