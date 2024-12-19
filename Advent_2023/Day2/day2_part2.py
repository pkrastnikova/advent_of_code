"""
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

def cube_games():
    f = open('day2_part1.txt', encoding="utf-8")

    result = 0

    for line in f:
        print(line)
        split_line = line.split(": ")        
        sets_part = split_line[1]        
        sets = sets_part.split("; ")

        red_cubes = list()
        green_cubes = list()
        blue_cubes = list()
        
        for set in sets:
            print(set)
            subsets = set.split(", ")
            for set in subsets:
                set_data = set.split(" ")                
                number_of_cubes = int(set_data[0], base=10)
                color_of_cubes = set_data[1].strip()
                print(set_data)
                if color_of_cubes == "red":
                    red_cubes.append(number_of_cubes)                    
                if color_of_cubes == "green":
                    green_cubes.append(number_of_cubes)                    
                if color_of_cubes == "blue":
                    blue_cubes.append(number_of_cubes)        

        game_power = max(red_cubes)*max(green_cubes)*max(blue_cubes)        

        result += game_power
           
    
    print("Final result: ", result)
    
    f.close()

cube_games()


