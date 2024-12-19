import numpy as np

f = open("day14_part1.txt", "r")

def move_rocks(grid):
    load = 0
   
    for j in range(len(grid[0])):
        for i in range(len(grid)):
            if grid[i][j] == "O":
                rock_load = len(grid) - i
                k = i-1
                while k >= 0:
                    if grid[k][j] == ".":
                        grid[k][j] = "O"
                        grid[k+1][j] = "."
                        rock_load += 1
                        k-=1
                    else:
                        break
            load += rock_load
    #print("Load: ", load)
    return grid

def count_load(grid):
    load = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "O":
                load += len(grid) - i
    print("Load: ", load)

                


line = f.readline().strip()
while True:
    grid = list()
    
    while len(line) > 1:
        row = list()
        for char in line:
            row.append(char)
        grid.append(row)
        line = f.readline().strip()
    # for i in range(len(grid)):
    #     for j in range(len(grid[0])):
    #         print(*grid[i][j], end="")
    #     print()
    
    print()           

    line = f.readline().strip()

    if not line:
        break


# print("Initial grid:")
# for row in grid:
#     print(row, end="\n")

grid = move_rocks(grid)
count_load(grid)

# print("Tilted grid:")
# for row in grid:
#     print(row, end="\n")



