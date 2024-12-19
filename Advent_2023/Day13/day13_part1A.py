import numpy as np

f = open("day13_part1_ex1.txt", "r")
#lines = f.readlines()

def find_mirror_columns(lines):
    result = 0
    
    for i in range(len(lines[0])-1):
        found_same = True
        print("i: ", i)
        for j in range(len(lines)-1):
            print(lines[j][i], lines[j][i+1])
            if lines[j][i] == lines[j][i+1]:            
                continue
            else:
                found_same = False
                break
        if found_same:
            result = i+1
            break
    print("Result: ", result)
    return result

def find_mirror_rows(lines):
    result = 0
    
    for i in range(len(lines)-1):
        if lines[i] == lines[i+1]:
            result = i + 1
            break
    return result

total_columns = 0
total_rows = 0
while True:
    line = f.readline()   
    lines = list()  
        
    while len(line) > 1:
        lines.append(line)        
        print(line) 
        line = f.readline()    
    print(lines) 
    mirror_columns = find_mirror_columns(lines)
    mirror_rows = find_mirror_rows(lines)
    print("Mirror columns: ", mirror_columns)
    print("Mirror rows: ", mirror_rows)
    
    total_columns += mirror_columns
    total_rows += mirror_rows

    
    if not line:
        break
print("Total reflection: ", total_columns + 100*total_rows)
    
    



# if line.strip():
#     ... do something



# for row in grid:
#     print(row, end="\n")

