import re
games = open("two.txt", "r").readlines()
counts = {
    "red": 12,
    "green": 13,
    "blue": 14
}

i = 1
total = 0
for game in games:
    rounds = re.sub(r"Game \d+: ", "", game).split("; ")
    for round in rounds:
        die = round.replace("\n", "").split(", ")
        for dice in die:
            data = dice.split(" ")
            if int(data[0]) > counts[data[1]]:
                # fail
                break
        else:
            # success
            continue
        break
    else:
        # success
        total += i
    i += 1
print(total)