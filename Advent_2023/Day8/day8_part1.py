f = open("day8_part1.txt", "r")

directions = f.readline().strip()



nodes = dict()
line = f.readline().strip()

while True:
    
    line = line.split(" ")
    #print(line)
    node = line[0]
    node_left = line[2]
    node_right = line[3]
    nodes[node] = (node_left[1:-1], node_right[:-1])

    line = f.readline().strip()
    

    if not line:
        break

#print(directions)
#print(nodes)

first = "AAA"
last = "ZZZ"
current = first
i = 0
steps = 0

while current != last:
    next_dir = directions[i]
    if next_dir == "L":
        next_dir = 0
    else:
        next_dir = 1

    next_node = nodes[current][next_dir]
    current = next_node

    steps += 1
    i += 1
    if i == len(directions):
        i = 0
    
print("Steps: ", steps)

