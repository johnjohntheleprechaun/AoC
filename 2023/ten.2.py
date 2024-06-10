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

touched_points = {start_pos}
pipe = [start_pos]


pipe_directions = {
    "|": [[-1,0], [1,0]],
    "-": [[0,-1], [0,1]],
    "L": [[-1,0], [0,1]],
    "J": [[-1,0], [0,-1]],
    "7": [[1,0], [0,-1]],
    "F": [[1,0], [0,1]],
    "S": [[-1,0], [1,0], [0,-1], [0,1]],
    ".": []
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

            # pipes are connected
            return next_pos 

def print_grid(marks):
    grid = [["." for x in range(len(tile_map[0]))] for y in range(len(tile_map))]
    for point in pipe:
        grid[point[0]][point[1]] = get_tile(point[0], point[1])
    for mark in marks:
        for point in mark[0]:
            grid[point[0]][point[1]] = mark[1]
    
    out = "\n".join(["".join(line) for line in grid])
    print(out)
    return out, grid

current_pos = find_next(start_pos)
touched_points.add(current_pos)
pipe.append(current_pos)

while get_tile(current_pos[0], current_pos[1]) != "S":
    current_pos = find_next(current_pos)
    
    if current_pos == None:
        break
    touched_points.add(current_pos)
    pipe.append(current_pos)


# replace S
d1 = [
    pipe[1][0] - pipe[0][0],
    pipe[1][1] - pipe[0][1]
]
d2 = [
    pipe[-1][0] - pipe[0][0],
    pipe[-1][1] - pipe[0][1]
]

for letter in pipe_directions:
    print(letter, pipe_directions[letter], d1, d2)
    if letter != "S" and d1 in pipe_directions[letter] and d2 in pipe_directions[letter]:
        print("thing")
        tile_map[pipe[0][0]][pipe[0][1]] = letter
        break

# pick start direction
start_dir = [pipe[1][0] - pipe[0][0], pipe[1][1] - pipe[0][1]]
side = 0 if start_dir.index(0) == 0 else 1
direction = start_dir
corner_vec = [0,0]
last_swap = False
for i in range(1, len(pipe)):
    tile = pipe[i]
    new_dir = [pipe[i][0]-pipe[i-1][0], pipe[i][1]-pipe[i-1][1]]
    if new_dir != direction:
        if i == len(pipe)-1:
            continue
        new_vec = [-direction[0] + new_dir[0], -direction[1] + new_dir[1]]
        vec_dif = [corner_vec[0]+new_vec[0], corner_vec[1]+new_vec[1]]
        if vec_dif == [0,0]:
            #print("180 swap")
            last_swap = True
            start_dir[side] = -start_dir[side]
        else:
            last_swap = False
        if corner_vec == [0,0]: # first corner
            start_dir[side] = new_dir[side]
        corner_vec = new_vec
    direction = new_dir




first_pos = (
    pipe[0][0]+(0 if start_dir[0] == 1 else -1),
    pipe[0][1]+(0 if start_dir[1] == 1 else -1) 
)

to_check = [first_pos]
checked = set()
enclosed = set()
directions = [
    [0,0],
    [1,0],
    [0,1],
    [1,1]
]

open("out.txt", "w").write(print_grid([])[0])
tile_map = print_grid([])[1]
while len(to_check) > 0:
    checks = []
    for direction in directions:
        check_position = (
            to_check[0][0] + direction[0],
            to_check[0][1] + direction[1]
        )
        if check_position[0] < 0 or check_position[1] < 0:
            continue
        checks.append(check_position)
        if check_position not in touched_points:
            enclosed.add(check_position)
    checked.add(to_check[0])

    up = [
        get_tile(to_check[0][0], to_check[0][1]),
        get_tile(to_check[0][0], to_check[0][1]+1)
    ]
    up_loc = (to_check[0][0]-1, to_check[0][1])
    if up_loc not in checked and ("." in up or ([0,1] not in pipe_directions[up[0]] and [0,-1] not in pipe_directions[up[1]])):
        #print("up")
        to_check.append(up_loc)
    
    down = [
        get_tile(to_check[0][0]+1, to_check[0][1]),
        get_tile(to_check[0][0]+1, to_check[0][1]+1)
    ]
    down_loc = (to_check[0][0]+1, to_check[0][1])
    if down_loc not in checked and ("." in down or ([0,1] not in pipe_directions[down[0]] and [0,-1] not in pipe_directions[down[1]])):
        #print("down")
        to_check.append(down_loc)
    
    left = [
        get_tile(to_check[0][0], to_check[0][1]),
        get_tile(to_check[0][0]+1, to_check[0][1])
    ]
    left_loc = (to_check[0][0], to_check[0][1]-1)
    if left_loc not in checked and ("." in left or ([1,0] not in pipe_directions[left[0]] and [-1,0] not in pipe_directions[left[1]])):
        #print("left")
        to_check.append(left_loc)
    
    right = [
        get_tile(to_check[0][0], to_check[0][1]+1),
        get_tile(to_check[0][0]+1, to_check[0][1]+1)
    ]
    right_loc = (to_check[0][0], to_check[0][1]+1)
    if right_loc not in checked and ("." in right or ([1,0] not in pipe_directions[right[0]] and [-1,0] not in pipe_directions[right[1]])):
        #print("right")
        to_check.append(right_loc)
    
    #print(up, down, left, right)
    #print(to_check[0])
    print_grid([[checked,"X"],[enclosed, "O"],[to_check[1:], "+"],[[to_check[0]],"0"]])
    #input()
    del to_check[0]
    to_check = list(set(to_check))

print(len(enclosed))