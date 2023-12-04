#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("Usage: {} <filename>".format(sys.argv[0]))
    sys.exit(1)

with open(sys.argv[1], "r") as f:
    lines = f.read().splitlines()


#####


def run():
    cards = {}
    for line in lines:
        card, numbers = line.split(":")
        card_num = int(card.split()[1])
        winning, drawn = ([int(x) for x in part.split()] for part in numbers.split("|"))
        cards[card_num] = {
            "num": card_num,
            "cardinality": 1,
            "points": len(set(winning).intersection(set(drawn))),
        }

    for _, card in cards.items():
        print(card)
        for _ in range(card["cardinality"]):
            for winned in range(card["points"]):
                cards[card["num"] + winned + 1]["cardinality"] += 1

    total_cardinality = sum(card["cardinality"] for card in cards.values())
    print(f"Total cardinality: {total_cardinality}")


if __name__ == "__main__":
    run()
