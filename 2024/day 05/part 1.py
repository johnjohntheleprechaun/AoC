import math
input_text = open("input.txt").read()

rules_string, updates_string = input_text.split("\n\n")

print(rules_string)

rules = {}

for rule in rules_string.splitlines():
    split_rule = rule.split("|")
    if split_rule[0] in rules:
        rules[split_rule[0]].append(split_rule[1])
    else:
        rules[split_rule[0]] = []
        rules[split_rule[0]].append(split_rule[1])

print(rules)

print(updates_string)
updates = []
for update_string in updates_string.splitlines():
    updates.append(update_string.split(","))

print(updates)

valid = 0
total = 0
for update in updates:
    for i, item in enumerate(update):
        previous = update[:i]
        for prev in previous:
            if item in rules and prev in rules[item]:
                break
        else:
            continue
        break
    else:
        valid += 1
        total += int(update[math.floor(len(update)/2)])

print(valid)
print(total)
