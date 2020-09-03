#To solve the N Queens problem with brute force technique (google the problem for more details)
#Do not enter 13 or more, will take A LOT of time

import itertools as it

def is_solution(perm):
    for (i1, i2) in it.combinations(range(len(perm)), 2):
        if abs(i1 - i2) == abs(perm[i1] - perm[i2]):
            return False

    return True

boardSize = int(input('Please enter the size of the board: '))

for perm in it.permutations(range(boardSize)):
    if is_solution(perm):
        print(perm)
        exit()