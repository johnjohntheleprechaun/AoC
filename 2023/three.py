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
    for check in checks:
        if check < 0 or check >= len(source):
            continue
        if re.match(r"[^.\d]", source[check]):
            return True
    return False


numbers = re.finditer(r"\d+", source)
total = 0
for number in numbers:
    
    for i in range(number.start(), number.end()):
        #print(source[i])
        if adjacent(i):
            print(number.group(0))
            print("added")
            total += int(number.group(0))
            break

print("first:",total)