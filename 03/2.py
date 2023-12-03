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
    parts = {}

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

    sum = 0
    for key in parts:
        if len(parts[key]) == 2:
            print(f"{key}: {parts[key]}")
            sum += parts[key][0] * parts[key][1]
    print(f"sum: {sum}")


def potential_part_number(i, j, digits):
    found = False
    for k in range(j - len(digits), j + 2):
        if k < 0 or k >= width:
            continue
        for m in range(i - 1, i + 2):
            if m == i and k in range(j - len(digits) + 1, j + 1):
                continue
            if m < 0 or m >= height:
                continue
            potential_part = grid[m][k]
            if not potential_part.isdigit() and not potential_part == ".":
                found = True
                if potential_part == "*":
                    if not (m, k) in parts:
                        parts[(m, k)] = []
                    parts[(m, k)].append(int(digits))
                break
            if found:
                break


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
