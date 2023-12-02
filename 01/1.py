#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("Usage: {} <filename>".format(sys.argv[0]))
    sys.exit(1)

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

numbers = []
for i in range(len(lines)):
    digits = []
    for c in lines[i]:
        if c.isnumeric():
            digits.append(c)
    if len(digits) == 0:
        raise (f"No digits found in line {i}")
    number_str = digits[0] + digits[-1]
    print(f"ligne {i}: {number_str}")
    numbers.append(int(number_str))

print(f"Sum: {sum(numbers)}")
