num = input()

num = int(num)

if num%2 != 0:
    print('Weird')
elif num > 2 and num < 5:
    print('Not Weird')
elif num > 6 and num < 20:
    print('Weird')
elif num > 20:
    print('Not Weird')
