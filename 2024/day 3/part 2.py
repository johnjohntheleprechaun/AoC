import re

regex = r"(?:do\(\))|(?:don't\(\))|(?:mul\((\d{1,3}),(\d{1,3})\))"

input_str = open("input.txt").read()

matches = re.finditer(regex, input_str, re.MULTILINE)

total = 0
enabled = True
for instruction in matches:
    if instruction.group(0) == "don't()":
        enabled = False
        continue
    elif instruction.group(0) == "do()":
        enabled = True
    elif enabled:
        total += int(instruction.group(1)) * int(instruction.group(2))

print(total)
