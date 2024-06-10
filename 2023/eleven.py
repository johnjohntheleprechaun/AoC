import numpy as np
from itertools import product
import math

input_data = open("eleven.txt", "r").read()
galaxy_map = np.array([[char for char in line] for line in input_data.split("\n")])
print(galaxy_map)
print(galaxy_map.shape)

emptyy = []
for y in range(galaxy_map.shape[0]):
    row = np.take(galaxy_map, y, 0)
    for item in row:
        if item != ".":
            break
    else:
        emptyy.append(y)

emptyx = []
for x in range(galaxy_map.shape[1]):
    column = np.take(galaxy_map, x, 1)
    for item in column:
        if item != ".":
            break
    else:
        emptyx.append(x)

print(emptyy, emptyx)

added = 0
for y in emptyy:
    galaxy_map = np.insert(galaxy_map, y+added, np.take(galaxy_map, y+added, 0), 0)
    added += 1
added = 0
for x in emptyx:
    galaxy_map = np.insert(galaxy_map, x+added, np.take(galaxy_map, x+added, 1), 1)
    added += 1

print(galaxy_map)
galaxies = []
for y in range(galaxy_map.shape[0]):
    for x in range(galaxy_map.shape[1]):
        if galaxy_map.item(y, x) == "#":
            galaxies.append((y,x))
print("galaxies: ", galaxies)
indices = [i for i in range(len(galaxies))]
combinations = set()
for i in range(len(indices)):
    for j in range(len(indices)):
        combinations.add(tuple(sorted((i,j))))
print(combinations)

total = 0
for combo in combinations:
    p1 = galaxies[combo[0]]
    p2 = galaxies[combo[1]]

    distance = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    print(combo, distance)
    total += distance
print(total)