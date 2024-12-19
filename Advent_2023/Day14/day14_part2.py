import numpy as np

f = open("day14_part1_ex1.txt", "r")

def rotate_grid(grid):

    rotated = [list(a) for a in zip(*grid[::-1])]
    print("Rotated: ")
    for i in range(len(rotated)):
        for j in range(len(rotated[0])):
            print(*rotated[i][j], end="")
        print()
    
    return rotated

def move_rocks(grid):   
   
    for j in range(len(grid[0])):
        for i in range(len(grid)):
            if grid[i][j] == "O":                
                k = i-1
                while k >= 0:
                    if grid[k][j] == ".":                        
                        grid[k][j] = "O"
                        grid[k+1][j] = "."                        
                        k-=1
                    else:
                        break            
   
    return grid

def perform_cycle(grid):
    for move in ("north", "west", "south", "east"):
        if move == "north":
            grid = move_rocks(grid)
        else:
            grid = move_rocks(rotate_grid(grid))

        print("Tilted grid: " + move)
        for row in grid:
            print(row, end="\n")

    return rotate_grid(grid)   

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
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(*grid[i][j], end="")
        print()
    
    print()           

    line = f.readline().strip()

    if not line:
        break


grid = perform_cycle(grid)
print("After one cycle:")
for row in grid:
    print(row, end="\n")
