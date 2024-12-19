
def calibration_value():
    f = open('day1_part1.txt', encoding="utf-8")
    result = 0    
    for line in f:
        number = ''
        for i in range(len(line)):
            #print("Char in line", line[i])
            if line[i].isnumeric():
                number += line[i]                    
        number = number[0] + number[-1]              
        result += int(number, base=10)               
    
    print("Result: ", result)   

    f.close()

calibration_value()