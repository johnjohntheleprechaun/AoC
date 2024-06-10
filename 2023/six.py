import re

input_data = open("six.txt", "r").read()
times = re.split(
    r" +",
    re.search("(?:Time: +)(.+)", input_data).group(1)
)
distances = re.split(
    r" +",
    re.search("(?:Distance: +)(.+)", input_data).group(1)
)
races = []
for i, time in enumerate(times):
    races.append([
        int(time), int(distances[i])
    ])

race_wins = []
for race in races:
    # find lower bounds
    lower = 0
    for i in range(race[0]+1):
        distance = (race[0] - i) * i
        if distance > race[1]:
            lower = i
            break
    print("lower", lower)

    upper = lower
    for i in range(upper, race[0] + 1):
        distance = (race[0] - i) * i
        print(distance)
        if distance <= race[1]:
            upper = i
            break
    print(upper)

    race_wins.append(upper-lower)

print(race_wins)
total = 1
for win in race_wins:
    total *= win
print(total)