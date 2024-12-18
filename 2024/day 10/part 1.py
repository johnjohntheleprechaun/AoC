import numpy as np

topograph = np.array([[int(char) for char in line] for line in open("input.txt").read().splitlines()])

print(topograph)

where = np.where(topograph == 9)
trailheads = list(zip(where[0], where[1]))

print(len(trailheads))
