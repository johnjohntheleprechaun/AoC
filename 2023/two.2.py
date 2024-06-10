import re
games = open("two.txt", "r").readlines()

i = 1
total = 0
for game in games:
    rounds = re.sub(r"Game \d+: ", "", game).split("; ")
    tops = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for round in rounds:
        die = round.replace("\n", "").split(", ")
        for dice in die:
            data = dice.split(" ")
            if int(data[0]) > tops[data[1]]:
                tops[data[1]] = int(data[0])
    total += tops["red"] * tops["green"] * tops["blue"]
    
print(total)