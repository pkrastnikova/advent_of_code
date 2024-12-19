f = open("day6_part1.txt", "r")

line_1 = f.readline().split(" ")
line_1 = [x.strip() for x in line_1 if x]      

line_2 = f.readline().split(" ")
line_2 = [x.strip() for x in line_2 if x]


races = [(line_1[1], line_2[1]), (line_1[2], line_2[2]), (line_1[3], line_2[3]), (line_1[4], line_2[4])]

print(line_1)
print(line_2)
print(races)

result = 1
for race in races:
    time = int(race[0])
    distance = int(race[1])
    count = 0

    for hold in range(1, time+1):
        remaining_time = time - hold
        traveled_dist = remaining_time*hold
        if traveled_dist > distance:
            count +=1

    result = result*count

print("Result: ", result)

