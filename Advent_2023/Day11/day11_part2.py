import numpy as np

f = open("day11_part1.txt", "r")

line = f.readline().strip()

grid = list()

while True:       
    grid.append(list(line))       
    line = f.readline().strip()    

    if not line:
        break

print("Initial grid:")
# for row in grid:
#     print(row, end="\n")

#Find empty column indexes
empty_indexes_2 = list()

for j in range(len(grid[0])):
    empty = True
    for i in range(len(grid)):
        if grid[i][j] == "#":
            empty = False
            break
    if empty:
        empty_indexes_2.append(j)
       
print("Empty col indexes: ", empty_indexes_2)


#Find empty row indexes
empty_indexes = list()

for i in range(len(grid)):
    if "#" not in grid[i]:
        empty_indexes.append(i)        
print("Empty row indexes: ", empty_indexes)  

    
#Create dict with galaxies
galaxies = dict()
index = 1
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '#':
            galaxies[index] = (i, j)
            index += 1
        #print(grid[i][j], end="")
    #print()
row_count = len(grid)
col_count = len(grid[0])
print(row_count, col_count)
print(galaxies)
print(index)  


def find_shortest_path(pair):
    point1 = pair[0]
    point2 = pair[1]
    x1 = galaxies[point1][0]
    y1 = galaxies[point1][1]
    x2 = galaxies[point2][0]
    y2 = galaxies[point2][1]
    row_offset = 0
    col_offset = 0
    for i in empty_indexes:
        if i in range(x1, x2) or i in range(x2, x1):
            row_offset += 1000000-1
    for i in empty_indexes_2:
        if i in range(y1, y2) or i in range(y2, y1):
            col_offset += 1000000-1

    
    return abs(x1-x2) + row_offset + abs(y1-y2)+ col_offset

result = 0

for i in range(1, len(galaxies.keys())+1):
    for j in range(i+1, len(galaxies.keys())+1):        
        result += find_shortest_path((i, j))

print("Result: ", result)
