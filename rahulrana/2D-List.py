# 2D Lists in python

number_grid = [
    #C1,2 ,3
    [1, 2, 3], # Row1
    [4, 5, 6], # Row2
    [7, 8, 9], # Row3
    [0]
]

print(number_grid[0][0], number_grid[0][1], number_grid[0][2])

for column in number_grid:
    for element in column:
        print(element, end=", ")

print("")
