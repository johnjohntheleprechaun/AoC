import re

regex = r"mul\((\d{1,3}),(\d{1,3})\)"

input_str = open("input.txt").read()

matches = re.finditer(regex, input_str, re.MULTILINE)

total = 0
for instruction in matches:
    print(instruction)
    print(instruction.group(1), instruction.group(2))
    total += int(instruction.group(1)) * int(instruction.group(2))

print(total)
