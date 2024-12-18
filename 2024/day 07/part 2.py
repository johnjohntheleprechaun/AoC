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

def traverse(target, current, nums, ops):
    if current > target:
        return False
    elif target == current and len(nums) == 0:
        return True
    if len(nums) == 0:
        return False
    if traverse(target, current * nums[0], nums[1:], ops):
        ops.append("*")
        return True
    elif traverse(target, int(str(current) + str(nums[0])), nums[1:], ops):
        ops.append("||")
        return True
    elif traverse(target, current + nums[0], nums[1:], ops):
        ops.append("+")
        return True
    else:
        return False

total = 0
valid = 0
for i, problem in enumerate(problems):
    target = problem[0]
    nums = problem[1]
    base = nums[0]

    ops = []
    if traverse(target, base, nums[1:], ops):
        total += target
        valid += 1

print(f"{valid} valid problems")
print(f"total: {total}")
