from itertools import product
import random

with open("input.txt", "w") as file:
    for combo in product("+*|", repeat=9):
        nums = [random.randrange(1000,100000) for i in range(10)]
        print(combo)
        total = nums[0]
        for i, num in enumerate(nums[1:]):
            if combo[i] == "+":
                total += num
            elif combo[i] == "*":
                total *= num
            elif combo[i] == "|":
                total = int(str(total) + str(num))
        file.write(f"{total}: {' '.join(str(num) for num in nums)}\n")
        file.write(" ".join(combo) + "\n")
