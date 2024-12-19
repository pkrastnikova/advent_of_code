def calibration_value():
    f = open('day1_part2_ex2.txt', encoding="utf-8")

    d = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9",
         "0":"0", "1":"1", "2":"2", "3":"3", "4":"4", "5":"5", "6":"6", "7":"7", "8":"8", "9":"9"}

    result = 0    
    for line in f:
        number = ''       
        min_number = ''        
        max_number = ''

        indeces_of_found = dict()
        print()
        print(line)
        for key in d.keys():
            index = line.rfind(key)            
            if index != -1:                
                indeces_of_found[index] = key
       
        sorted_keys = sorted(indeces_of_found.keys())
        print(sorted_keys)

        first_index = indeces_of_found[sorted_keys[0]]       
        last_index = indeces_of_found[sorted_keys[-1]]
        print(first_index, last_index)

        first_last = d[first_index] + d[last_index]
        print(first_last)
            
        result += int(first_last, base=10)               
    
    print("Result: ", result)   

    f.close()

calibration_value()