f = open("day9_part1.txt", "r")

def find_next_lines(line):

    all_next_lines = list()
    all_next_lines.append(line)
    
    while True:
        next_line = list()        
        for i in range(len(line)-1):
            next_line.append(line[i+1]-line[i])
        all_next_lines.append(next_line)
        
        if next_line.count(0) == len(next_line):
            break
        else:
            line = next_line
            continue
    #print("All next lines: ", all_next_lines)
    return all_next_lines

def extrapolate(lines):
    last_value = 0

    for i in reversed(range(len(lines))):
        current_line = lines[i]
        next_value = current_line[0] - last_value
        last_value = next_value
    return next_value


result = 0
line = f.readline().strip()

while True:
    
    line = line.split(" ")
    line = [int(i) for i in line]
    next_lines = find_next_lines(line)
    next_value = extrapolate(next_lines)
   
    result += next_value
    

    line = f.readline().strip()
    

    if not line:
        break


print("Result: ", result)







                         