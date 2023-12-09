#!/usr/bin/env python3
import sys
from functools import reduce

if len(sys.argv) != 2:
    print("Usage: {} <filename>".format(sys.argv[0]))
    sys.exit(1)


#####


def run(fh):
    acc = 0
    for l in fh:
        numbers = [int(x) for x in l.split()]
        # print(numbers)
        previous = [numbers[0]]
        while not all([x == 0 for x in numbers]):
            numbers = next_row(numbers)
            previous.append(numbers[0])
            # print(numbers)

        computed_previous = reduce(lambda i, j: j - i, reversed(previous))

        acc += computed_previous
        # print(f"previous: {previous}, computed: {computed_previous}, acc: {acc}")

    print(acc)


def next_row(row):
    return [j - i for i, j in zip(row, row[1:])]


if __name__ == "__main__":
    with open(sys.argv[1]) as fh:
        run(fh)
