import math

f = open('day4_part1.txt', "r")
lines = f.readlines()
result = 0

for line in lines:
    line.strip()
    split_line = line.split(": ")
    split_data = split_line[1].strip().split("|")
    win_numbers = split_data[0].strip().split()
    my_numbers = split_data[1].strip().split()
    print(win_numbers)
    print(my_numbers)
    points = 0 
    first = True
    for number in win_numbers:
        if number in my_numbers:    
            if first:
                points = 1
                first = False
            else: 
                points = points*2  
                    
            print("Points: ", points)
                   
        
    result += points

print(result)



