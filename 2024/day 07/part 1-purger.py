import re

print("parsing input...")

text_input = open("input.txt").read()

problems = []
for line in text_input.splitlines():
    result = re.match(r"(\d+): ((?:\d+ ?)+)", line)
    if result == None:
        continue
    problems.append((int(result.group(1)), [int(num) for num in result.group(2).split(" ")]))

print(f"found {len(problems)} problems")

def traverse(target, current, nums):
    if current > target:
        return False
    elif target == current:
        return True
    if len(nums) == 0:
        return False
    if traverse(target, current * nums[0], nums[1:]):
        return True
    elif traverse(target, current + nums[0], nums[1:]):
        return True
    else:
        return False

total = 0
file = open("input.txt", "w")
for problem in problems:
    target = problem[0]
    nums = problem[1]
    base = nums[0]

    if traverse(target, base, nums[1:]):
        total += target
    else:
        file.write(f"{target}: {' '.join(str(num) for num in nums)}\n")

print(total)
