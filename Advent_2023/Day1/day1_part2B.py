#right solution optimized

def calibration_value():
    f = open('day1_part2.txt', encoding="utf-8")

    d = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9",
         "0":"0", "1":"1", "2":"2", "3":"3", "4":"4", "5":"5", "6":"6", "7":"7", "8":"8", "9":"9"}
    
    result = 0    
    for line in f:        
        numbers_found = list()
        print()
        print(line)
        
        for i in range(len(line)):  
                word = ''          
                k = 0 #number of letters in word built (5 max)
                j = i 
                while j < len(line) and k < 5:   
                    word = word + line[j]                 
                    if word in d: #check if constructed string is a number
                        numbers_found.append(word)
                        break
                    else:
                        j += 1
                        k += 1                      
        
        first_last = d[numbers_found[0]] + d[numbers_found[-1]]

        print(first_last)
            
        result += int(first_last, base=10)               
    
    print("Result: ", result)   

    f.close()

calibration_value()