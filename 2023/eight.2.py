import re
import numpy as np

input_data = open("eight.txt", "r").read()

map_iter = re.finditer(r"(.{3}) = \((.{3}), (.{3})\)", input_data)
maps = {}
for map in map_iter:
    maps[map.group(1)] = [map.group(2), map.group(3)]
print(maps)

directions = [0 if direction == "L" else 1 for direction in re.match(r"(?:R|L)+", input_data).group(0)]

positions = []
for position in maps.keys():
    if position[-1] == "A":
        positions.append(position)

cycles = []
for start in positions:
    position = start
    z_hits = 0
    iters = 0
    while position[-1] != "Z":
        direction = directions[iters % len(directions)]
        position = maps[position][direction]
        iters += 1

    cycles.append(iters)
print(cycles)

print(np.lcm.reduce(cycles))