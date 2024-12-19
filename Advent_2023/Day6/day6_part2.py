f = open("day6_part1.txt", "r")

line_1 = f.readline().replace(" ", "").rstrip().split(":")     

line_2 = f.readline().replace(" ", "").rstrip().split(":")

races = [(line_1[1], line_2[1])]

print(line_1)
print(line_2)
print(races)

result = 1
for race in races:
    time = int(race[0])
    distance = int(race[1])
    count = 0
    no_win = False

    for hold in range(1, time + 1):
        remaining_time = time - hold
        traveled_dist = remaining_time * hold
        if traveled_dist > distance:
            count +=1
        elif traveled_dist < distance and count > 1:
            if no_win == False:
                no_win = True
            else:
                break

    result = result*count

print("Result: ", result)

