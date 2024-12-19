import numpy as np

f = open("day13_part1.txt", "r")
result = 0
def transpose_grid(grid):   
    transposed = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
    print("Transposed: ")
    # for i in range(len(transposed)):
    #     for j in range(len(transposed[0])):
    #         print(*transposed[i][j], end="")
    #     print()
    return transposed

def find_reflection_rows(grid, direction):        
    refl = list()
    for i in range(len(grid)-1):
        if grid[i] == grid[i+1]:     
            if i == 0:
                refl.append([1, 0, direction])
                continue
            if i == len(grid) - 2:
                refl.append([i+1, i, direction])
                continue

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
                              
            if found:            
                refl.append([i+1, i, direction])               
                                                 
    return refl

def check_for_reflections(grid):   
    print("Check for reflections: ")
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(*grid[i][j], end="")
        print()
    reflections_h = find_reflection_rows(grid, "h")         
    
    reflections_v = find_reflection_rows(transpose_grid(grid), "v")    

    print("Found reflections: ", reflections_h + reflections_v)

    return reflections_h + reflections_v

def check_for_original(grid):   
    print("Check for original, h")
    reflections = list()   
    reflections = find_reflection_rows(grid, "h")    
    if len(reflections) == 0:      
        reflections= find_reflection_rows(transpose_grid(grid), "v")    
    
    return reflections
    
def find_smudge(grid):
    result = 0
    found_reflection = False
    original_reflection = check_for_original(grid)[0]    
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

            print("i, j: ", i, j)
            # if i==9 and j == 1:
            #     for i in range(len(grid)):
            #        for j in range(len(grid[0])):
            #          print(*grid[i][j], end="")
            #        print()                       
           
            new_reflections = check_for_reflections(grid)            
            
            print("new refl", new_reflections)
            if len(new_reflections) > 0:

                for reflection in new_reflections:
                    if reflection != original_reflection:
                        if reflection[2] == "h":
                            result += reflection[0]*100
                        else:
                            result += reflection[0]
                        
                        found_reflection = True
                        break
            grid[i][j] = current_value                
            if found_reflection:
                break
        if found_reflection:
                break
    print("Found original reflection: ", original_reflection)
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





