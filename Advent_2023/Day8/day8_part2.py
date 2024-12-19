f = open("day8_part1.txt", "r")

directions = f.readline().strip()



nodes = dict()
first = list()
last = list()

line = f.readline().strip()

while True:
    
    line = line.split(" ")
    #print(line)
    node = line[0]
    node_left = line[2]
    node_right = line[3]
    nodes[node] = (node_left[1:-1], node_right[:-1])

    if node[-1] == "A":
        first.append(node)
    if node[-1] == "Z":
        last.append(node)

    line = f.readline().strip()
    

    if not line:
        break

#print(directions)
#print(nodes)
print(first)
print(last)


current = first
i = 0
steps = 0

# while True:
#     next_dir = directions[i]
#     if next_dir == "L":
#         next_dir = 0
#     else:
#         next_dir = 1
    
#     next_nodes = list()
    
#     for node in current:
#         next_nodes.append(nodes[node][next_dir])
    
#     current = next_nodes

#     steps += 1
#     i += 1
#     if i == len(directions):
#         i = 0

#     no_z_end_found = False
    
#     #print("Next nodes: ", next_nodes)
    
#     for node in next_nodes:
#         if node[-1] != "Z":
#             no_z_end_found = True
#             break
#     if no_z_end_found:
#         continue
#     else:
#         break
    
# print("Steps: ", steps)

