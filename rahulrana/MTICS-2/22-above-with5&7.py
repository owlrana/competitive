#program to give back the no. of change (5s and 7s) above 24 for given input

def change( amount ):
    assert(amount >= 24)
    
    if amount == 24:
        return [5, 5, 7, 7]
    if amount == 25:
        return [5, 5, 5, 5, 5]
    if amount == 26:
        return [5, 7, 7, 7]
    if amount == 27:
        return [5, 5, 5, 5, 7]
    if amount == 28:
        return [7, 7, 7, 7]

    coins = change(amount - 5)
    coins.append(5)
    return coins

amount = int(input('Please enter the amount above 24 you want: '))
print(change(amount))