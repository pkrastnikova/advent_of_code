import sys
#DO NOT USE LISTS OR RANGES OR ITERATIONS WITHIN SOURCE!!! Track only the start and end element of each range.


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
        map.sort(key=lambda x: int(x[1]))
    return line

# source start, source end - start and end int of the source
# maps - [[dest, source, count], [dest, source, count],...]
# return subranges from source, mapped to ranges from map   
def find_subranges_in_map(source_start, source_end, maps):
    #print("find subranges")
    #print("Source: ", source)
    #source_start = int(source[0])
    #source_end = int(source[-1])
    found_ranges = list()
    current_point = source_start
    
    for map in maps:     
        map_start = int(map[1])
        map_end = int(map[1] + map[2] - 1)
        
        if map_start <= source_start and map_end >= source_end: 
            #print("case 1")                       
            found_ranges.append(convert_mapped_ranges(map, [source_start, source_end]))            
            #print("Found ranges: ", found_ranges) 
            current_point = source_end           
            break
        elif map_start > source_end or map_end < source_start:   
            #print("case 2")                   
            #print("range outside source")
            continue
        elif map_start < current_point and map_end < source_end:
            #print("case 3") 
            new_range = convert_mapped_ranges(map, [current_point, map_end])            
            found_ranges.append(new_range)
            #print("Found partial range: ", found_ranges)
            current_point = map_end + 1
        elif map_start >= current_point and map_end <= source_end:
            #print("case 4") 
            if map_start > current_point:
                new_range_1 = [current_point, map_start-1]
                found_ranges.append(new_range_1)
            new_range_2 = convert_mapped_ranges(map, [map_start, map_end])            
            found_ranges.append(new_range_2)
            #print("Found range within source: ", found_ranges)
            current_point = map_end + 1
        elif map_start >= current_point and map_end > source_end:
            #print("case 5")
            if map_start > current_point:
                new_range_1 = [current_point, map_start -1]
                found_ranges.append(new_range_1)
            new_range_2 = convert_mapped_ranges(map, [map_start, source_end])            
            found_ranges.append(new_range_2)
            #print("Found ranges: ", found_ranges)
            current_point = source_end
            break
    # if current_point == source_start:
    #     found_ranges.append(source)
    if current_point < source_end:
        found_ranges.append([current_point, source_end])
    #print("Found ranges(final for this source): ", found_ranges)
    return found_ranges
            



# map_entry - [dest, source, count]
# source - [source_start, source_end]
# return - [mapped_start, mapped_end]
def convert_mapped_ranges(map_entry, source):
    offset = map_entry[0] - map_entry[1]  # difference between source and destination value
    return [source[0] + offset, source[1] + offset]
   
def sort_ranges_in_map(map):
    return map.sort(key=lambda x: int(x[1]))

line = f.readline()

while True:        

    first_string = line.split(" ")[0]

    if first_string.startswith("seeds"):
        # create list with seeds
        numbers = line.split(" ")[1:]
        
        i = 0
        while i < len(numbers):
            #seeds_list = list(range(int(numbers[i]), int(numbers[i]) + int(numbers[i+1].rstrip())))
            seeds_list = [int(numbers[i]), int(numbers[i+1])]
            i += 2
            seeds.append(seeds_list)
        
        #print("Seeds: ", seeds)
        line = f.readline()      
   
    elif first_string.startswith("seed-to-soil"):
        #print("create seed-to-soil map")                    
        line = read_lines_with_ranges(seed_to_soil)
        #print(seed_to_soil)  
           
    elif first_string.startswith("soil-to-fertilizer"):
        #print("create soil-to-fertilizer map")        
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

min_location = sys.maxsize

# seeds = list(range(79, 79+14))
# seed_to_soil_map = [[50, 98, 2], [52, 50, 48]]
# soil_to_fertilizer_map = [[0, 15, 37], [37, 52, 2], [39, 0, 15]]

# print("Seeds: ", seeds)
# seed_to_soil = find_subranges_in_map(seeds[0], seed_to_soil)
# print(seed_to_soil)
# print("Seed_to_soil: ", seed_to_soil)
# soil_to_fertilizer = find_subranges_in_map(seed_to_soil[0], soil_to_fertilizer)
# print(soil_to_fertilizer)

for seed_range in seeds:
    #print("Seeds: ", seed_range)
    soils = find_subranges_in_map(seed_range[0], seed_range[0]+seed_range[1]-1, seed_to_soil)
    #print("Soils: ", soils)
    for soil_range in soils:
        fertilizers = find_subranges_in_map(soil_range[0], soil_range[-1], soil_to_fertilizer)
        #print("Fertilizers: ", fertilizers)
        for fert_range in fertilizers:
            waters = find_subranges_in_map(fert_range[0], fert_range[-1], fertilizer_to_water)
            #print("Waters: ", waters)
            for water_range in waters:                
                lights = find_subranges_in_map(water_range[0], water_range[-1], water_to_light)
                #print("Lights: ", lights)
                for light_range in lights:
                    temperatures = find_subranges_in_map(light_range[0], light_range[-1], light_to_temperature)
                    #print("Temperatures: ", temperatures)
                    for temp_range in temperatures:
                        humidities = find_subranges_in_map(temp_range[0], temp_range[-1], temperature_to_humidity)
                        #print("Humidities: ", humidities)
                        for hum_range in humidities:                            
                            locations = find_subranges_in_map(hum_range[0], hum_range[-1], humidity_to_location)
                            #print("Hum. range, Locations: ", hum_range, locations)
                            
                            for location in locations:
                                #print("Location: ", location)
                                min_element = min(location)
                                if min_element < min_location:
                                    min_location = min_element
                                    
    
       
print("Lowest location: ", min_location)




 



