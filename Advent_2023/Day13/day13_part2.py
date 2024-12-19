import numpy as np

f = open("day13_part1_ex3.txt", "r")
result = 0
def transpose_grid(grid):   
    transposed = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
    print("Transposed: ")
    for i in range(len(transposed)):
        for j in range(len(transposed[0])):
            print(*transposed[i][j], end="")
        print()
    return transposed

def find_reflection_rows(grid, direction, original=None):    
    counter = 0
    for i in range(len(grid)-1):
        if grid[i] == grid[i+1]:     
            if i == 0:
                return [1, 0, direction]
            if i == len(grid) - 2:
                return [i+1, i, direction]

            k = i+2
            j = i-1
             
            while j >= 0 and k <= len(grid)-1:
                if grid[j] == grid[k]:                    
                    found = True
                else:
                    found = False
                    break
                j -= 1
                k += 1           
                              
            if found and original == None:            
                counter = i+1               
                break
            if found and i == original[1]:
                continue
            if found and i != original[1]:
                counter = i+1
                break

    if counter == 0:
        return None   
    else:                                        
        return [counter, counter-1, direction]

def check_for_reflection(grid, original):
    print("Check for reflection, h")
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(*grid[i][j], end="")
        print()
    reflection = find_reflection_rows(grid, "h", original)
    print("reflection h: ", reflection)
    if reflection == None or reflection == original:
        reflection = find_reflection_rows(transpose_grid(grid), "v", original)
        print("reflection v: ", reflection)
    return reflection
    
def find_smudge(grid):
    result = 0
    found_reflection = False
    original_reflection = check_for_reflection(grid, None)
    print("Test grid: ")
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(*grid[i][j], end="")
        print()
    print("Original reflection: ", original_reflection)
  
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            current_value = grid[i][j]
            if grid[i][j] == ".":
                grid[i][j] = "#"                
            else:
                grid[i][j] = "."
                       
            #print("Replaced: ")    
             
            #search for new reflection
            
            new_reflection = check_for_reflection(grid, original_reflection)
            if (new_reflection == None) or (new_reflection == original_reflection):
                grid[i][j] = current_value
                continue
            else:
                print("new refl", new_reflection)
                if new_reflection != None:
                    if new_reflection[2] == "h":
                        result += new_reflection[0]*100
                    else:
                        result += new_reflection[0]
                    grid[i][j] = current_value
                    found_reflection = True

            if found_reflection:
                break
        if found_reflection:
            break
    print("Found smudge result: ", result)
    return result



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

    result += find_smudge(grid)        

    line = f.readline().strip()

    if not line:
        break

print("Result: ", result)




