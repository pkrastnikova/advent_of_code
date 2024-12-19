import sys

f = open("day5_part1_ex.txt", "r")

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

    
# source - list of integers
# map - [[dest, source, count], [dest, source, count],...]
# return subranges from source, mapped to ranges from map
def find_subranges_in_map(source, map):
    
    start_point = source[0]
    end_point = source[-1]
    
    current_point = start_point
    found_subranges = list()        
    found_map = -1
    mapped_value = True

    while current_point <= end_point:     
        #print("Current point: ", current_point)   
        found_map = find_point_in_map(current_point, map)  # return [dest, source, count]                 

        if found_map == -1:          # current point not found in any map -> continue        
            if current_point == end_point: # source end is reached
                #print("start, end point: ", start_point, end_point)
                found_subranges.append(list(range(start_point, end_point + 1)))
                break
            else:
                current_point += 1                
                mapped_value = False
                continue

        else: # current point found in a map
            #print("current point found in a map: ", current_point)
            found_map_source = found_map[1]
            found_map_count = found_map[2]
            found_map_source_end_point =  found_map_source + found_map_count - 1
            #print("Found map end point: ", found_map_source_end_point)

            #create subrange for previous non-mapped values
            if mapped_value == False:                
                found_subranges.append(list(range(start_point, current_point)))
            
            #process found mapped range               
            if end_point > found_map_source_end_point:
                found_subranges.append(convert_mapped_ranges(found_map, list(range(current_point, found_map_source_end_point+1))))
                start_point = found_map_source + found_map_count 
                current_point = start_point
                mapped_value = True
                continue
            else:
                found_subranges.append(convert_mapped_ranges(found_map, list(range(current_point, end_point + 1))))
                break
            
    return found_subranges


# map - [[dest, source, count], [dest, source, count],...]
# return entry [dest, source, count] from map where the point belongs to
# return -1 if point not part of any entry in the map
def find_point_in_map(point, map):
    for entry in map:
        source_start = entry[1]
        source_end = entry[1] + entry[2]
        if point in range(source_start, source_end):
            return entry  #[dest, source, count]
    return -1

# map_entry - [dest, source, count]
# source - list of integeres
# return list of mapped values
def convert_mapped_ranges(map_entry, source):
    offset = map_entry[0] - map_entry[1]  # difference between source and destination value
    return list(range(source[0] + offset, source[-1] + offset + 1))
   


line = f.readline()

while True:        

    first_string = line.split(" ")[0]

    if first_string.startswith("seeds"):
        # create list with seeds
        numbers = line.split(" ")[1:]
        #print(numbers)

        i = 0
        while i < len(numbers):
            seeds_list = list(range(int(numbers[i]), int(numbers[i]) + int(numbers[i+1].rstrip())))
            i += 2
            seeds.append(seeds_list)
        
        #print("Seeds: ", seeds)
        line = f.readline()      
   
    elif first_string.startswith("seed-to-soil"):
        #print("create seed-to-soil map")                    
        line = read_lines_with_ranges(seed_to_soil)
        print(seed_to_soil)  
           
    elif first_string.startswith("soil-to-fertilizer"):
        #print("create soil-to-fertilizer map")        
        line = read_lines_with_ranges(soil_to_fertilizer)        
        print(soil_to_fertilizer)

    elif first_string.startswith("fertilizer-to-water"):
        #print("create fertilizer_to_water map")
        line = read_lines_with_ranges(fertilizer_to_water)
        print(fertilizer_to_water)

    elif first_string.startswith("water-to-light"):
        #print("create water_to_light map")
        line = read_lines_with_ranges(water_to_light)
        print(water_to_light)

    elif first_string.startswith("light-to-temperature"):
        #print("create light_to_temperature map")
        line = read_lines_with_ranges(light_to_temperature)
        print(light_to_temperature)
   
    elif first_string.startswith("temperature-to-humidity"):
        #print("create temperature_to_humidity map")
        line = read_lines_with_ranges(temperature_to_humidity)
        print(temperature_to_humidity)
   
    elif first_string.startswith("humidity-to-location"):
        #print("create humidity_to_location map")
        line = read_lines_with_ranges(humidity_to_location)
        print(humidity_to_location)

    else:
        line = f.readline()          
   

    # if line is empty
    # end of file is reached
    if not line:
        break

min_location = sys.maxsize


for seed_range in seeds:
    print("Seeds: ", seed_range)
    soils = find_subranges_in_map(seed_range, seed_to_soil)
    print("Soils: ", soils)
    for soil_range in soils:
        fertilizers = find_subranges_in_map(soil_range, soil_to_fertilizer)
        print("Fertilizers: ", fertilizers)
        for fert_range in fertilizers:
            waters = find_subranges_in_map(fert_range, fertilizer_to_water)
            print("Waters: ", waters)
            for water_range in waters:                
                lights = find_subranges_in_map(water_range, water_to_light)
                print("Lights: ", lights)
                for light_range in lights:
                    temperatures = find_subranges_in_map(light_range, light_to_temperature)
                    print("Temperatures: ", temperatures)
                    for temp_range in temperatures:
                        humidities = find_subranges_in_map(temp_range, temperature_to_humidity)
                        print("Humidities: ", humidities)
                        for hum_range in humidities:                            
                            locations = find_subranges_in_map(hum_range, humidity_to_location)
                            print("Hum. range, Locations: ", hum_range, locations)
                            
                            for location in locations:
                                print("Location: ", location)
                                min_element = min(location)
                                if min_element < min_location:
                                    min_location = min_element
                                    
    
       

print("Lowest location: ", min_location)




 



