import numpy as np

start_grid = np.array([[item for item in row] for row in open("input.txt").read().splitlines()])
where_am_i = np.where(start_grid == "^")
start_pos = (where_am_i[0][0], where_am_i[1][0])

movements = [
    (-1,0),
    (0,1),
    (1,0),
    (0,-1),
]
marks = ["^", ">", "v", "<"]

def go_to_end(pos, direction, grid):
    move_set = set()
    position_set = set()
    moves = []
    while True:
        next_pos = (pos[0] + movements[direction][0], pos[1] + movements[direction][1])
        grid[pos] = marks[direction]
        if next_pos[0] < 0 or next_pos[0] >= grid.shape[0] or next_pos[1] < 0 or next_pos[1] >= grid.shape[1]:
            move = (pos, direction)
            moves.append(move)
            move_set.add(move)
            position_set.add(pos)
            break

        if grid[next_pos] == "#":
            #print("turn")
            direction = (direction + 1) % 4
        else:
            #print("move")
            move = (pos, direction)
            if move in move_set:
                return "loop"
            moves.append(move)
            move_set.add(move)
            position_set.add(pos)
            pos = next_pos
    return moves, move_set, position_set

things = go_to_end(start_pos, 0, start_grid.copy())

if things == "loop":
    quit()

print(len(things[2]))

count = 0
blocks = []
for i, move in enumerate(things[0][::-1]):
    if i == len(things[0]):
        continue
    print(len(things[0]) - i)
    test_grid = start_grid.copy()
    #for pos in things[0][:-(i+1)]:
    #    test_grid[pos[0]] = "X"
    test_grid[move[0]] = "#"
    result = go_to_end(start_pos, 0, test_grid)
    if result == "loop":
        blocks.append(move[0])
        count += 1
print(count, len(set(blocks)))
