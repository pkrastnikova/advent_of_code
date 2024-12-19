f = open("day7_part1.txt", "r")


def find_type(hand):
    print("Hand: ", hand)
    d = dict()
    for letter in hand:
        if ranks.index(letter) in d.keys():
            d[ranks.index(letter)]+=1
        else:
            d[ranks.index(letter)] = 1
    
    
    print("d0: ", d)
    if 0 in d.keys():
        num_j = d[0]
            
        print("num_j:", num_j)

        d_sorted = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        print("d_sorted: ", d_sorted)

        for key in d_sorted.keys():
            if key != 0:
                d[key] += num_j
                del d[0]
                break
        
          

    num_keys = len(d.keys())

    print("d: ", d)

    if num_keys == 1:
        return 6
    elif num_keys == 2:
        if 4 in d.values():
            return 5
        else:
            return 4
    elif num_keys == 3:
        if 3 in d.values():
            return 3
        else:
            return 2
    elif num_keys == 4:
        return 1
    else:
        return 0


ranks = "J23456789TQKA"
my_hands = list()

line = f.readline()

while True:
    line = line.strip().split(" ")
    hand = line[0]
    bid = line[1]

    hand_type = find_type(hand)
    print("Hand type: ", hand_type)
    hand_rankes = list()
    for letter in hand:
        rank = ranks.index(letter)
        hand_rankes.append(rank)
    hand_rankes = tuple(hand_rankes)
    my_hands.append((hand_type, *hand_rankes, bid))
    

    line = f.readline()
    if not line:
        break
    
my_hands = sorted(my_hands)
result = 0
i = 1

print("my_hands: ", my_hands)

for hand in my_hands:         
    bid = int(hand[-1])     
    result += i*bid
    i+=1

#print(my_hands)  
print("Result: ", result)     