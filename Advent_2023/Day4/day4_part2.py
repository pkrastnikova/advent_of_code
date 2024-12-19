f = open('day4_part1.txt', "r")
lines = f.readlines()
result = 0

d = {} #key - line(card) index; value - number of matches
f = {} #key - line(card) index; value - number of cards per index (original + copies)

for i in range(len(lines)):
    lines[i].strip()
    split_line = lines[i].split(": ")
    split_data = split_line[1].strip().split("|")
    win_numbers = split_data[0].strip().split()
    my_numbers = split_data[1].strip().split()
    #print(win_numbers)
    #print(my_numbers)
    count = 0
    
    for number in win_numbers:
        if number in my_numbers:    
            count+=1
    d[i+1] = count 
    
    f[i+1] = 1        #add key for each card with value 1 (1 card initially)   
 
#copy cards
for i in range(1, len(lines)+1): 
    matching_count = d[i]    
    for j in range(1, matching_count+1):        
        f[i+j] += f[i]   

result = 0
for key in f.keys():
    result += f[key]

print("Total number of cards: ", result)
    



                   
        
    




