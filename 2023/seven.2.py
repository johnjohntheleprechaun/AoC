from functools import cmp_to_key
import json

hands = [hand.split(" ") for hand in open("seven.txt", "r").read().split("\n")]

def get_type(hand):
    sorted_hand = sorted([item for item in hand])
    
    start = 0
    counts = [0]
    jokers = 1 if sorted_hand[0] == "J" else 0
    for i in range(1,len(sorted_hand)):
        if sorted_hand[i] == "J":
            jokers += 1
            start = i
            continue
        if sorted_hand[i] == sorted_hand[start]:
            counts[-1] += 1
        else:
            counts.append(0)
            start = i
    print(sorted_hand)
    print(counts)
    print(jokers)
    if jokers == 5:
        return 6
    
    
    # add to max
    counts[counts.index(max(counts))] += jokers
    print(counts)

    if sum(counts) == 0: # High card
        print("high card")
        return 0
    elif sum(counts) == 1: # One pair
        print("one pair")
        return 1
    elif counts.count(1) == 2: # Two pair
        print("two pair")
        return 2
    elif counts.count(2) == 1 and sum(counts) == 2: # Three of a kind
        print("three of a kind")
        return 3
    elif counts.count(2) == 1 and counts.count(1) == 1: # Full house
        print("full house")
        return 4
    elif counts.count(3) == 1: # Four of a kind
        print("four of a kind")
        return 5
    if counts.count(4) == 1: # Five of a kind
        print("five of a kind")
        return 6

score_map = {
    "T": 10,
    "J": 1,
    "Q": 12,
    "K": 13,
    "A": 14
}
def get_score(card: str):
    if card.isnumeric():
        return int(card)
    else:
        return score_map[card]
file = open("out.txt", "a")
def compare(first, second):
    print("\n\n")
    first = first[0]
    second = second[0]
    type1 = get_type(first)
    type2 = get_type(second)
    if type1 == type2:
        print("MATCHING")
        # compare better
        for i, card in enumerate(first):
            if get_score(card) > get_score(second[i]):
                print(first, second)
                return 1
            elif get_score(card) < get_score(second[i]):
                print(second, first)
                return -1
        return 0
        
    else:
        return type1 - type2

sorted_hands = sorted(hands, key=cmp_to_key(compare))
file = open("out.json", "w")
json.dump(sorted_hands, file)
total = 0
for i, hand in enumerate(sorted_hands):
    total += int(hand[1]) * (i+1)

print(get_type("QJQJT"))
print(total)