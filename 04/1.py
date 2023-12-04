#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("Usage: {} <filename>".format(sys.argv[0]))
    sys.exit(1)

with open(sys.argv[1], "r") as f:
    lines = f.read().splitlines()


#####


def run():
    recap = []
    for line in lines:
        card, numbers = line.split(":")
        card_num = int(card.split()[1])
        winning, drawn = ([int(x) for x in part.split()] for part in numbers.split("|"))
        # winning, drawn = numbers.split("|")
        # winning = [int(x) for x in winning.split()]
        # drawn = [int(x) for x in drawn.split()]
        print(f"card: {card_num}, winning: {winning}, drawn: {drawn}")

        points = 0
        for num in winning:
            if num in drawn:
                points = 1 if points == 0 else points * 2
            else:
                continue
        recap.append((card_num, points))

    print(recap)
    points_sum = sum(x for _, x in recap)
    print(f"points_sum: {points_sum}")


if __name__ == "__main__":
    run()
