# check if range is part of another range
# range, subrange - lists of consequitive int values
def check_subrange_in_range(range, subrange):
    if subrange[0] >= range[0] and subrange[-1] <= range[-1]:
        return True
    return False

# check if part of range r1 belongs to range r2
# return subrange from r1 that is part of r2
# example: r1 = [3,4,5,6,7], r2 = [5,6,7,8,9]; returns [5,6,7]
def check_part_of_range(r1, r2):
    if r1[0] >= r2[0] and r1[-1] >= r2[-1]:
        return range(r1[0], r2[-1] + 1)
    return False

# remove subrange from a range
# return remaining range
def remove_subrange(range, subrange):
    print("range: ", range)
    print("subrange: ", subrange)
    for item in subrange:
        if item in range:
            range.remove(item)
    return list(range)



# get mapped ranges for range r1; if subrange cannot map, return the same subrange
def get_ranges(r1, r2, r3):
    print("Original list: ", list(r1))
    mapped_ranges = list()
    map_r2 = check_part_of_range(r1, r2)
    print("start 2: ", map_r2.start)  
    print("count 2: ", len(list(map_r2)))
    map_r3 = check_part_of_range(r1, r3)
    print("start 3: ", map_r3.start)
    r1 = list(remove_subrange(list(r1), list(map_r2)))
    r1 = list(remove_subrange(list(r1), list(map_r3)))
    print("r1: ", r1)
    mapped_ranges.append(r1)
    if map_r2:
        mapped_ranges.append(list(map_r2))
        print("mapped_ranges: ", mapped_ranges)
    if map_r3:
        mapped_ranges.append(list(map_r3))
        print("mapped_ranges: ", mapped_ranges)
    return mapped_ranges


# source - list of integers
# map - [[dest, source, count], [dest, source, count],...]]
# return subranges from source mapped to ranges from map
def find_subranges_in_maps2(source, map):
    
    start_point = source[0]
    end_point = source[-1]
    
    current_point = start_point
    found_subranges = list()        
    found_map = -1
    mapped_value = True

    while current_point <= end_point:        
        found_map = find_point_in_maps2(current_point, map)  # return [dest, source, count]
                 

        if found_map == -1:          # current point not found in any map -> continue with next number            
            if current_point == end_point: # source end is reached
                print("start, end point: ", start_point, end_point)
                found_subranges.append(list(range(start_point, end_point + 1)))
                break
            else:
                current_point += 1                
                mapped_value = False
                continue

        else: # current point found in a map
            print("current point found in a map")
            found_map_dest = found_map[0]
            found_map_source = found_map[1]
            found_map_count = found_map[2]
            found_map_source_end_point =  found_map_source + found_map_count - 1

            #create subrange for previous non-mapped values
            if mapped_value == False:                
                found_subranges.append(list(range(start_point, current_point)))
            
            #process found mapped range  
             
            if end_point > found_map_source_end_point:
                found_subranges.append(convert_mapped_ranges(found_map, list(range(current_point, found_map_source_end_point+1))))
                start_point = found_map_source + found_map_count + 1
                current_point = start_point
                mapped_value = True
                continue
            else:
                found_subranges.append(convert_mapped_ranges(found_map, list(range(current_point, end_point + 1))))
                break
            
    return found_subranges

 
def find_point_in_maps(point, maps):
    for map in maps:
        if point in range(map[0], map[-1] + 1):
            return map
    return -1

# map - [[dest, source, count], [dest, source, count],...]]
# return entry [dest, source, count] from map where the point belongs to
# return -1 if point not part of any entry in the map
def find_point_in_maps2(point, map):
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
    offset = map_entry[0] - map_entry[1]  # difference between source and destination values
    return list(range(source[0] + offset, source[-1] + offset + 1))



r1 = [1, 2, 3, 4, 5, 6, 7]
r2 = [0, 1, 2, 3, 4]
r3 = [5, 6, 7]

r4 = range(51, 100) # (51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66 ..., 99)
r5 = range(53, 61)  # (53, 54, 55, 56, 57, 58, 59, 60)
r6 = range(62, 65)  # (62, 63, 64)
r7 = range(70, 120)
maps = [list(r5), list(r6), list(r7)]

#seeds: 79 14 55 13

#seed-to-soil map:
#50 98 2
#52 50 48

#soil-to-fertilizer map:
#0 15 37
#37 52 2
#39 0 15

seeds = list(range(79, 79+14))
seed_to_soil_map = [[50, 98, 2], [52, 50, 48]]
soil_to_fertilizer_map = [[0, 15, 37], [37, 52, 2], [39, 0, 15]]

print("Seeds: ", seeds)
seed_to_soil = find_subranges_in_maps2(seeds, seed_to_soil_map)
print("Seed_to_soil: ", seed_to_soil)
soil_to_fertilizer = find_subranges_in_maps2(seed_to_soil[0], soil_to_fertilizer_map)

print("Soil to fert: ", soil_to_fertilizer)
lis = sorted([[1,4,7],[3,6,9],[2,59,8]])
print(lis)

li = [[1,14,7],[3,5,9],[2,1,8]]
li.sort(key=lambda x: int(x[1]))
print(li)

#print(find_subranges_in_maps2(r4, maps))

