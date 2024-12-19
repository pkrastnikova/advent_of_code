import numpy as np

f = open("day13_part1_ex3.txt", "r")
result = 0
def transpose_grid(grid):
    #transposed = list()
    transposed = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
    
    for i in range(len(transposed)):
        for j in range(len(transposed[0])):
            print(*transposed[i][j], end="")
        print()
    return transposed

def find_reflection_rows(grid):
    #print("Find reflection rows:")
    counter = 0
    for i in range(len(grid)-1):
        if grid[i] == grid[i+1]:
            # print("First duplicates: ")
            # print(*grid[i])
            # print(*grid[i+1])

            if i == 0:
                return 1
            if i == len(grid) - 2:
                return i+1

            #print("Next reflections:")
            k = i+2
            j = i-1
             
            while j >= 0 and k <= len(grid)-1:
                if grid[j] == grid[k]:
                    #print(*grid[j])
                    #print(*grid[k], counter)                    
                    found = True
                else:
                    found = False
                    break
                j -= 1
                k += 1           
                              
            if found:                
                #print("Number of reflection rows: ", counter)             
                counter = i+1
                break
                                        
    return counter
 

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
    found_rows = find_reflection_rows(grid)
    print("Found rows: ", found_rows)
    if found_rows != None:
        result += found_rows*100
            
    print("Transposed grid: ")
    
    found_columns = find_reflection_rows(transpose_grid(grid))
    print("Found columns: ", found_columns)
    if found_columns != None:
        result += found_columns
        

    line = f.readline().strip()

    if not line:
        break

print("Result: ", result)




