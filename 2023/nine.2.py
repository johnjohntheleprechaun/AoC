input_data = open("nine.txt", "r").read().split("\n")

lines = [[[int(num) for num in line.split(" ")]] for line in input_data]

for i, param in enumerate(lines):
    while not sum(lines[i][-1]) == 0:
        lines[i].append([])
        for j in range(1, len(lines[i][-2])):
            lines[i][-1].append(lines[i][-2][j] - lines[i][-2][j-1])

total = 0
for line in lines:
    num = 0
    for level in reversed(line):
        print(level)
        num = level[0] - num
        print(num)
    total += num
    print("added", num)
print("total", total)