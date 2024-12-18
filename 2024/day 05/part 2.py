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

def rule_based_sort(update):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i, item in list(enumerate(update))[::-1]:
            if item not in rules:
                continue
            previous = update[:i]

            invalid = []
            for j, prev in enumerate(previous):
                if prev in rules[item]:
                    invalid.append(j)
                    is_sorted = False
            invalid.sort()
            for j, index in enumerate(invalid):
                update.append(update[index-j])
                del update[index-j]
    return update


total = 0
for update in updates:
    sorted_update = rule_based_sort(update.copy())
    if sorted_update != update:
        print(sorted_update)
        total += int(sorted_update[math.floor(len(sorted_update)/2)])

print(total)
