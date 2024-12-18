from itertools import product
import random

nums = [random.randrange(1,100) for i in range(10)]
with open("input.txt", "w") as file:
    for combo in product("+*", repeat=len(nums)-1):
        total = nums[0]
        for i, num in enumerate(nums[1:]):
            if combo[i] == "+":
                total += num
            elif combo[i] == "*":
                total *= num
        file.write(f"{total}: {' '.join(str(num) for num in nums)}\n")
        file.write(" ".join(combo) + "\n")
