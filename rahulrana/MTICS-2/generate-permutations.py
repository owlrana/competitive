#program to generate all possible permutations with recursion

def generate_permutations(perm, n):
    if len(perm) == n:
        print(perm)
        return

    for k in range(n):
        if k not in perm:
            perm.append(k)
            generate_permutations(perm, n)
            perm.pop()

#Either do this:
n = int(input('Enter the size of board you want to permutate for: '))
perm = []
generate_permutations(perm, n)

#or do:
# generate_permutations(perm = [], n = 4) 
# don't do ...(perm = [], n) or ...(perm, n = x)
# this gives the error or positional & keyword argument
# https://stackoverflow.com/questions/53605836/syntax-error-positional-argument-follows-keyword-argument/53605863