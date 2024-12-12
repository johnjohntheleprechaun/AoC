import numpy as np

grid = np.array([[item for item in row] for row in open("input.txt").read().splitlines()])
where_am_i = np.where(grid == "^")
pos = (where_am_i[0][0], where_am_i[1][0])

movements = [
    (-1,0),
    (0,1),
    (1,0),
    (0,-1),
]
moves = []
move_set = set()
position_set = set()

direction = 0
while True:
    next_pos = (pos[0] + movements[direction][0], pos[1] + movements[direction][1])
    if next_pos[0] < 0 or next_pos[0] >= grid.shape[0] or next_pos[1] < 0 or next_pos[1] >= grid.shape[1]:
        move = (pos, direction)
        moves.append(move)
        move_set.add(move)
        position_set.add(pos)
        break

    if grid[next_pos] == "#":
        direction = (direction + 1) % 4
    else:
        move = (pos, direction)
        moves.append(move)
        move_set.add(move)
        position_set.add(pos)
        pos = next_pos

print(len(position_set))
