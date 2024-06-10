import re

cards = [re.sub(r"Card \d+: ", "",card).split(" | ") for card in open("four.txt", "r").read().split("\n")]

total = 0
for card in cards:
    card_score = 0
    winners = re.split(r" +", card[0])
    numbers = re.split(r" +", card[1])
    for number in numbers:
        if number in winners:
            if card_score == 0:
                card_score = 1
            else:
                card_score *= 2
    print(card_score)
    total += card_score
    print("FINSIHED")
print(total)