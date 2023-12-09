#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("Usage: {} <filename>".format(sys.argv[0]))
    sys.exit(1)


#####


def run(fh):
    acc = 0
    for l in fh:
        numbers = [int(x) for x in l.split()]
        # print(numbers)
        next = [numbers[-1]]
        while not all([x == 0 for x in numbers]):
            numbers = next_row(numbers)
            next.append(numbers[-1])
            # print(numbers)
        computed_next = sum(next)
        acc += computed_next
        # print(f"next: {next}, sum: {sum(next)} computed: {computed_next}")

    print(acc)


def next_row(row):
    return [j - i for i, j in zip(row, row[1:])]


if __name__ == "__main__":
    with open(sys.argv[1]) as fh:
        run(fh)
