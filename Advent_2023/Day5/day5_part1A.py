import sys

f = open("day5_part1.txt", "r")

seeds = list()
seed_to_soil = list()
soil_to_fertilizer = list()
fertilizer_to_water = list()
water_to_light = list()
light_to_temperature = list()
temperature_to_humidity = list()
humidity_to_location = list() 

def read_lines_with_ranges(map):  
    while True:
        line = f.readline()
        if line and line[0][0].isdigit():
            number_line_split = line.split(" ")
            dest = int(number_line_split[0].rstrip())
            source = int(number_line_split[1].rstrip())
            count = int(number_line_split[2].rstrip())
            map.append([dest, source, count])                     
        else:                
            break
    return line

def find_value_in_map(map, source):
    for entry in map:
        source_start = entry[1]
        source_end = entry[1] + entry[2]
        dest_start = entry[0]        
        if source in range(source_start, source_end):           
            offset = source - source_start
            return dest_start + offset
    return source



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
        print("create fertilizer_to_water map")
        line = read_lines_with_ranges(fertilizer_to_water)
        #print(fertilizer_to_water)

    elif first_string.startswith("water-to-light"):
        print("create water_to_light map")
        line = read_lines_with_ranges(water_to_light)
        #print(water_to_light)

    elif first_string.startswith("light-to-temperature"):
        print("create light_to_temperature map")
        line = read_lines_with_ranges(light_to_temperature)
        #print(light_to_temperature)
   
    elif first_string.startswith("temperature-to-humidity"):
        print("create temperature_to_humidity map")
        line = read_lines_with_ranges(temperature_to_humidity)
        #print(temperature_to_humidity)
   
    elif first_string.startswith("humidity-to-location"):
        print("create humidity_to_location map")
        line = read_lines_with_ranges(humidity_to_location)
        #print(humidity_to_location)

    else:
        line = f.readline()          
   

    # if line is empty
    # end of file is reached
    if not line:
        break

min_location = sys.maxsize
min_seed = seeds[0]

for seed in seeds:
    soil = find_value_in_map(seed_to_soil, int(seed))
    fertilizer = find_value_in_map(soil_to_fertilizer, int(soil))
    water = find_value_in_map(fertilizer_to_water, int(fertilizer))
    light = find_value_in_map(water_to_light, int(water))
    temperature = find_value_in_map(light_to_temperature, int(light))
    humidity = find_value_in_map(temperature_to_humidity, int(temperature))
    location = int(find_value_in_map(humidity_to_location, int(humidity)))

    #print(seed, soil, fertilizer, water, light, temperature, humidity, location)

    if location < min_location:
        min_location = location
        min_seed = seed

print("Lowest location: ", min_location)




 



