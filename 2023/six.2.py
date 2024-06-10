import re

input_data = open("six.txt", "r").read()
race = [int(num) for num in re.sub(
    r"(?:Distance:)| +|(?:Time:)",
    "",
    input_data
).split("\n")]
print(race)


lower = 0
for i in range(race[0]+1):
    distance = (race[0] - i) * i
    if distance > race[1]:
        lower = i
        break
upper = lower
for i in range(upper, race[0] + 1):
    distance = (race[0] - i) * i
    if distance <= race[1]:
        upper = i
        break

possible = upper-lower
print(possible)