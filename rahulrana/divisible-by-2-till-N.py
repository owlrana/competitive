# Given an integer N, find how many pairs of distinct integers from 0 to N - 1 sum up to an even value.
# N is positive and does not exceed 100,000

def divisible_pairs(n):
    ans = 0
    for i in range(n):
        for j in range(n):
            if i < j and (i + j)%2 == 0:
                ans += 1
                print(i ,",", j)
    return ans

n = int(input("Enter the value of n to find the no. of distinct pairs that add up to an even number: "))

print(divisible_pairs(n))