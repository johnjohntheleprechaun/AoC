import numpy as np

input_dat = np.array([[char for char in row] for row in open("input.txt").read().splitlines()], dtype=object)
input_data = np.full((input_dat.shape[0] + 2, input_dat.shape[1] + 2), "~")
print(input_data.shape)
input_data[1:-1,1:-1] = input_dat
locations = np.where(input_data == "^")
location = (locations[0][0], locations[1][0])
ahead = (location[0]-1, location[1])
print(location)
print(input_data.item(location))

obstacles = np.where(input_data == "#")
print(obstacles)
for i in range(len(obstacles[0])):
    pos = (obstacles[0][i],obstacles[1][i])
    print(pos)
    input_data[pos] = "#" + str(i)
    print(input_data[pos])

input_data[location] = "X"

print(input_data)
print("----------------------")
while True:
    if input_data[ahead][0] == "#":
        input_data[location] = "^"
        input_data = np.rot90(input_data)
        locations = np.where(input_data == "^")
        location = (locations[0][0], locations[1][0])
        ahead = (location[0]-1, location[1])
        input_data[location] = "X"
    elif input_data[ahead] == "~":
        break
    else:
        input_data = np.roll(input_data, 1, 0)
        input_data[location] = "X"
    print(input_data[location[0]-4:location[0]+5,location[1]-4:location[1]+5])
    #input()

for row in input_data:
    print("".join(row))
print(np.count_nonzero(input_data == "X"))
