import numpy as np

f = open("day13_part1_ex2.txt", "r")

result = 0
counter = 1
current_line = f.readline().strip()

while True:       
    
    next_line = f.readline().strip()
    counter += 1 

    if not next_line:
        break

    print(current_line)
    print(next_line)
    print()
    if current_line == next_line:        
        result = counter - 1
        break
    else:
        current_line = next_line

print("Result: ", result)


print("Initial grid:")
# for row in grid:
#     print(row, end="\n")

