import re
data = open("one.txt", "r").readlines()

regexp = r"one|two|three|four|five|six|seven|eight|nine|\d"
num_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

numbers = []
for line in data:
    # get the first digit
    i = 0
    while not re.search(regexp, line[:i]):
        i += 1
    first = re.search(regexp, line[:i]).group(0)
    first_dig = first if len(first) == 1 else num_map[first]

    i = -1
    while not re.search(regexp, line[i:]):
        i -= 1
    last = re.search(regexp, line[i:]).group(0)
    last_dig = last if len(last) == 1 else num_map[last]
    
    numbers.append(int(first_dig + last_dig))
print(str(sum(numbers)))

exit()












def get_int(data: str):
    if data.isnumeric():
        return data
    else:
        return str(num_map[data])
    
numbers = []
out = open("out.txt", "a")
for line in data:
    digits = re.findall(regexp, line)

    first = digits[0] if len(digits[0]) == 1 else str(num_map[digits[0]])
    last = digits[-1] if len(digits[-1]) == 1 else str(num_map[digits[-1]])
    print(first + last)
    print(line)
    
    out.write(line)
    out.write(first + last + "\n\n")
    numbers.append(int(first + last))
print(sum(numbers))