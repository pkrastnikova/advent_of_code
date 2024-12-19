import math
d = {}
star = (0, 1)
d[star] = [123]
print(d)

d[star].append(234)

print(d)

for count in range(1, 5):
    point = count*2
    print(point)


