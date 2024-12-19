import sys

f = open("day5_part1_ex.txt", "r")

seeds = list()
seed_to_soil = dict()
soil_to_fertilizer = dict()
fertilizer_to_water = dict()
water_to_light = dict()
light_to_temperature = dict()
temperature_to_humidity = dict()
humidity_to_location = dict()

def fib_a(start, end):
    a = start
    while a < end:
        yield a
        a += 1

def fib_b(start, end):
    b = start
    while b < end:
        yield b
        b += 1      
     
def add_to_source_dest_map2(map, line):
   
    number_line_split = line.split(" ")
    dest = int(number_line_split[0].rstrip())
    source = int(number_line_split[1].rstrip())
    count = int(number_line_split[2].rstrip())
   
    x = fib_a(source, source + count)
    y = fib_b(dest, dest + count)
   
    for i, j in zip(x, y):        
        map[i] = j                   

    return map

def add_to_source_dest_map(map, line):
   
    number_line_split = line.split(" ")
    dest = int(number_line_split[0].rstrip())
    source = int(number_line_split[1].rstrip())
    count = int(number_line_split[2].rstrip())

    for i in range(count):
        map[source] = dest
        source += 1
        dest += 1      

    return map


def read_lines_with_ranges(map):  
    while True:
        line = f.readline()
        if line and line[0][0].isdigit():
            map = add_to_source_dest_map2(map, line)   # run for each number line            
        else:                
            break
    return line

def find_value_in_map(map, value):
    if value in map.keys():
        return map.get(int(value))
    else:
        return int(value)

   
line = f.readline()

while True:        

    first_string = line.split(" ")[0]

    if first_string.startswith("seeds"):
        # create list with seeds
       
        for number in line.split(" ")[1:]:
            seeds.append(number.rstrip())
        #seeds = sorted(seeds)
        print(seeds)
        line = f.readline()      
   
    elif first_string.startswith("seed-to-soil"):
        print("create seed-to-soil map")                    
        line = read_lines_with_ranges(seed_to_soil)            
        #print(seed_to_soil)  
           
    elif first_string.startswith("soil-to-fertilizer"):
        print("create soil-to-fertilizer map")        
        line = read_lines_with_ranges(soil_to_fertilizer)        
        #print(soil_to_fertilizer)

    elif first_string.startswith("fertilizer-to-water"):
        #print("create fertilizer_to_water map")
        line = read_lines_with_ranges(fertilizer_to_water)
        #print(fertilizer_to_water)

    elif first_string.startswith("water-to-light"):
        #print("create water_to_light map")
        line = read_lines_with_ranges(water_to_light)
        #print(water_to_light)

    elif first_string.startswith("light-to-temperature"):
        #print("create light_to_temperature map")
        line = read_lines_with_ranges(light_to_temperature)
        #print(light_to_temperature)
   
    elif first_string.startswith("temperature-to-humidity"):
        #print("create temperature_to_humidity map")
        line = read_lines_with_ranges(temperature_to_humidity)
        #print(temperature_to_humidity)
   
    elif first_string.startswith("humidity-to-location"):
        #print("create humidity_to_location map")
        line = read_lines_with_ranges(humidity_to_location)
        #print(humidity_to_location)

    else:
        line = f.readline()          
   

    # if line is empty
    # end of file is reached
    if not line:
        break

min_locatiion = sys.maxsize
min_seed = seeds[0]

for seed in seeds:
    soil = find_value_in_map(seed_to_soil, seed)
    fertilizer = find_value_in_map(soil_to_fertilizer, soil)
    water = find_value_in_map(fertilizer_to_water, fertilizer)
    light = find_value_in_map(water_to_light, water)
    temperature = find_value_in_map(light_to_temperature, light)
    humidity = find_value_in_map(temperature_to_humidity, temperature)
    location = int(find_value_in_map(humidity_to_location, humidity))

    #print(seed, soil, fertilizer, water, light, temperature, humidity, location)

    if location < min_locatiion:
        min_locatiion = location
        min_seed = seed

print("Lowest location: ", min_locatiion)
#print(seed_to_soil.get(int('79')))



 



