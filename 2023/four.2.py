import re
import json

data = open("four.txt", "r").read()
card_regex = r"Card +(\d+): +((?:\d+ *)+) \| +((?:\d+ *)+)"
card_data = re.finditer(card_regex, data, re.MULTILINE)
cards = []


for i, card in enumerate(card_data):
    winning = re.split(" +", card.group(2))
    numbers = re.split(" +", card.group(3))
    cards.append([1, set(winning), numbers])


for i, card in enumerate(cards):
    #print(i, card)
    # run the card
    matched = 0
    for num in card[2]:
        if num in card[1]:
            matched += 1
    for j in range(card[0]):
        
        for k in range(matched):
            cards[i+k+1][0] += 1


# count cards
total = 0
for card in cards:
    total += card[0]
print(total)