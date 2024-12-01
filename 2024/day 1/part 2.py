input_text = open("input.txt").readlines()

list_1 = []
list_2 = []

for line in input_text:
    split = line.split("   ")
    list_1.append(int(split[0]))
    list_2.append(int(split[1]))

total = 0
for num in list_1:
    total += list_2.count(num) * num

print(total)
