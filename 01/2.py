#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("Usage: {} <filename>".format(sys.argv[0]))
    sys.exit(1)

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

numbersmap = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

numbers = []
for i in range(len(lines)):
    digits = []
    for j in range(len(lines[i])):
        if lines[i][j].isnumeric():
            digits.append(lines[i][j])
        else:
            for key, value in numbersmap.items():
                if lines[i][j : j + len(key)] == key:
                    digits.append(str(value))
                    break
    if len(digits) == 0:
        raise (f"No digits found in line {i}")
    number_str = digits[0] + digits[-1]
    print(f"ligne {i}: {number_str}")
    numbers.append(int(number_str))

print(f"Sum: {sum(numbers)}")
