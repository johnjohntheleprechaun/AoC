data = open("one.txt", "r").readlines()
numbers = []
for line in data:
    # get the first digit
    i = 0
    while not line[i].isnumeric():
        i += 1
    first = line[i]

    i = -1
    while not line[i].isnumeric():
        i -= 1
    last = line[i]
    
    numbers.append(int(first + last))
print(str(sum(numbers)))