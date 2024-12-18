import numpy as np
from itertools import combinations

grid = np.array([[char for char in row] for row in open("input.txt", "r").read().splitlines()])
print(grid)

antennas = {}

it = np.nditer(grid, flags=["multi_index"])

for item in it:
    item = str(item)
    if item == ".":
        continue
    if item not in antennas:
        antennas[item] = []
    antennas[item].append(it.multi_index)

print(antennas)
def in_bounds(node):
    if node[0] >= 0 and node[0] < grid.shape[0] and node[1] >= 0 and node[1] < grid.shape[1]:
        return True

antinodes = set()
for frequency in antennas:
    for a, b in combinations(antennas[frequency], 2):
        diff = (a[0] - b[0], a[1] - b[1])
        antinodes.add(a)
        antinodes.add(b)

        i = 1
        a_node = (a[0] + diff[0] * i, a[1] + diff[1] * i)
        while in_bounds(a_node):
            i += 1
            antinodes.add(a_node)
            a_node = (a[0] + diff[0] * i, a[1] + diff[1] * i)

        i = 1
        b_node = (b[0] - diff[0] * i, b[1] - diff[1] * i)
        while in_bounds(b_node):
            i += 1
            antinodes.add(b_node)
            b_node = (b[0] - diff[0] * i, b[1] - diff[1] * i)

        print(f"points {a} and {b} have a distance of {diff}")

for node in antinodes:
    grid[node] = "#"
print(grid)
print(len(antinodes))
