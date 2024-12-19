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
offset = 0
for j in range(len(grid[0])):
    empty = True
    for i in range(len(grid)):
        if grid[i][j] == "#":
            empty = False
            break
    if empty:
        empty_indexes_2.append(j+1+offset)
        offset +=1
print("Empty col indexes: ", empty_indexes_2)

#Duplicate empty columns
for i in range(len(grid)):    
    #print(i, grid[i])
    for k in empty_indexes_2:               
        grid[i].insert(k, ".")  
 
# for row in grid:    
#     print(row, end="\n")

#Create empty row
empty_row = list()
for i in range(len(grid[0])):
    empty_row.append(".")
print("Len(empty_row): ", len(empty_row))

#Find empty row indexes
empty_indexes = list()
offset = 0
for i in range(len(grid)):
    if "#" not in grid[i]:
        empty_indexes.append(i+1+offset)
        offset+=1
print("Empty row indexes: ", empty_indexes)
    
#Insert empty rows
for i in empty_indexes:
    grid.insert(i, empty_row)


print("Len(grid): ", len(grid))
    

# print("Final grid expanded:")
# for i in range(len(grid)):    
#     print(grid[i], end="\n")
    
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
    return abs(x1-x2) + abs(y1-y2)

result = 0

for i in range(1, len(galaxies.keys())+1):
    for j in range(i+1, len(galaxies.keys())+1):        
        result += find_shortest_path((i, j))

print("Result: ", result)
