import re

source = open("three.txt", "r").read()
width = len(source.split("\n")[0])
source = source.replace("\n", "")
height = len(source) // width
grid = [[letter for letter in line] for line in source.split("\n")]
for row in grid:
    print("".join(row))
print(len(grid), len(grid[0]))

def adjacent(index: int):
    checks = [
        index-width-1, index-width, index-width+1,
        index-1, index, index+1,
        index+width-1, index+width, index+width+1
    ]
    adjacence = []
    ignore = []
    for check in checks:
        if re.match(r"\d", source[check]):
            if check in ignore:
                continue
            start = check
            while re.match(r"\d", source[start]):
                ignore.append(start)
                start -= 1
            start += 1
            end = check
            while re.match(r"\d", source[end]):
                ignore.append(end)
                end += 1

            print(source[start:end])
            adjacence.append(int(source[start:end]))
    return adjacence

total = 0
numbers = [re.finditer(r"\d+", source)]
for i, letter in enumerate(source):
    if letter == "*":
        adjacence = adjacent(i)
        if len(adjacence) == 2:
            total += adjacence[0] * adjacence[1]

print(total)