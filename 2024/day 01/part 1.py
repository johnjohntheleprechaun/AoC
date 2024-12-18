import math
input_text = open("input.txt").readlines()

list_1 = []
list_2 = []

for line in input_text:
    split = line.split("   ")
    list_1.append(int(split[0]))
    list_2.append(int(split[1]))

list_1.sort()
list_2.sort()

total = 0
for i in range(len(list_1)):
    total += abs(list_1[i] - list_2[i])

print(total)
