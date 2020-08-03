#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# wrong output in input: 1 -1 -2 -1; -7 -7 -7 -7 6; 57 57 -57 57;

#take the input
num = int(input())

#analyse the input
while num <= 2 or not num <= 10:    
    num = int(input())

scores = input()    #input the scores with space bar in b/w
score_list = scores.split()  #store the scores into a list, remember: the values are still strings

#initialize the highest and runner ups
high = 0
runner = -1

#loop to check and assign the values
for i in range(num):
    if int(score_list[i]) > high:
        runner = high
        high = int(score_list[i])
    if int(score_list[i]) > runner:
            if int(score_list[i]) < high:
                runner = int(score_list[i])
        
print(runner)