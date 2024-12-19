from math import lcm

f = open("day8_part1.txt", "r")

directions = f.readline().strip()

nodes = dict()
first = list()
last = list()

line = f.readline().strip()

while True:    
    line = line.split(" ")
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

print(first)
print(last)


def find_steps(node, directions):
    current = node
    i = 0
    steps = 0
    
    while current[-1] != "Z":
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
    print("Found: ", current)
    return steps

steps = list()

for node in first:
    steps.append(find_steps(node, directions))

print("Steps: ", steps)

print("Result: ", lcm(*steps))







