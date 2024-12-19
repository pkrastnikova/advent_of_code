f = open("day7_part1.txt", "r")


def find_type(hand):
    d = dict()
    for letter in hand:
        if letter in d.keys():
            d[letter]+=1
        else:
            d[letter] = 1
    num_keys = len(d.keys())
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


ranks = "23456789TJQKA"
my_hands = list()

line = f.readline()

while True:
    line = line.strip().split(" ")
    hand = line[0]
    bid = line[1]

    hand_type = find_type(hand)
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

for hand in my_hands:         
    bid = int(hand[-1])     
    result += i*bid
    i+=1

#print(my_hands)  
print("Result: ", result)     