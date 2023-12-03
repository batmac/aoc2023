#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("Usage: {} <filename>".format(sys.argv[0]))
    sys.exit(1)

with open(sys.argv[1], "r") as f:
    lines = f.read().splitlines()


#####


def run():
    global grid, height, width, parts
    grid = []
    parts = []

    for line in lines:
        grid.append(list(line))
    # dump_grid(grid)
    height = len(grid)
    width = len(grid[0])

    for i in range(height):
        digits = ""
        for j in range(width):
            if grid[i][j].isdigit():
                digits += grid[i][j]
            else:
                if len(digits) == 0:
                    continue
                potential_part_number(i, j - 1, digits)
                digits = ""

        if len(digits) > 0:
            potential_part_number(i, width - 1, digits)
            digits = ""
    print(f"parts: {parts}")
    print("sum: {}".format(sum(parts)))


def potential_part_number(i, j, digits):
    # i,j is the position of the last digit
    # print(f"potential_part_number: {digits}")
    found = False
    for k in range(j - len(digits), j + 2):
        if k < 0 or k >= width:
            continue
        for m in range(i - 1, i + 2):
            if m == i and k in range(j - len(digits) + 1, j + 1):
                continue
            if m < 0 or m >= height:
                continue
            if not grid[m][k].isdigit() and not grid[m][k] == ".":
                found = True
                break
            if found:
                break
    if found:
        parts.append(int(digits))


def dump_grid(grid):
    height = len(grid)
    width = len(grid[0])
    for row in grid:
        if len(row) != width:
            raise ("Error: row width mismatch")
        print("".join(row))
    print("height: {}, width: {}".format(height, width))


if __name__ == "__main__":
    run()
