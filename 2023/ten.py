import math

input_data = open("ten.txt", "r").read()
tile_map = []
lines = input_data.split("\n")
start_pos = []
for y in range(len(lines)):
    tile_map.append([])
    for x in range(len(lines[y])):
        tile_map[-1].append(lines[y][x])
        if tile_map[y][x] == "S":
            start_pos = (y, x)

def get_tile(y, x):
    if y < 0 or x < 0 or y >= len(tile_map) or x >= len(tile_map[0]):
        return "."
    else:
        return tile_map[y][x]

def get_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

print(start_pos)
print(tile_map)
touched_points = {start_pos}


pipe_directions = {
    "|": [[-1,0], [1,0]],
    "-": [[0,-1], [0,1]],
    "L": [[-1,0], [0,1]],
    "J": [[-1,0], [0,-1]],
    "7": [[1,0], [0,-1]],
    "F": [[1,0], [0,1]],
    "S": [[-1,0], [1,0], [0,-1], [0,1]]
}
def find_next(current):
    directions = pipe_directions[get_tile(current[0], current[1])]
    for direction in directions:
        next_pos = (current[0]+direction[0], current[1]+direction[1])
        next_pipe = get_tile(next_pos[0], next_pos[1])

        reverse_dir = [direction[0] * -1, direction[1] * -1]


        
        if next_pipe == ".":
            continue
        if next_pos not in touched_points and reverse_dir in pipe_directions[next_pipe]:
            print(next_pipe)
            # pipes are connected
            return next_pos 


farthest = start_pos
farthest_steps = 0
steps = 1
current_pos = find_next(start_pos)
touched_points.add(current_pos)

while get_tile(current_pos[0], current_pos[1]) != "S":
    current_pos = find_next(current_pos)
    steps += 1
    
    if current_pos == None:
        break
    
    print(steps, "steps")
    touched_points.add(current_pos)
    if get_distance(start_pos, current_pos) > get_distance(start_pos, farthest):
        # new farthest
        farthest = current_pos
        farthest_steps = steps

print(farthest)

print("TOTAL")
print(int(steps/2))