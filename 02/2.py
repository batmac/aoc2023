#!/usr/bin/env python3

import re
import sys

if len(sys.argv) != 2:
    print("Usage: {} <filename>".format(sys.argv[0]))
    sys.exit(1)

with open(sys.argv[1], "r") as f:
    lines = f.read().splitlines()


r_game = re.compile(r"^Game (\d+):(.*)$")
r_draw = re.compile(r"(?: (?P<cubes>\d+) (?P<color>blue|red|green))+")

minimum_powers = []
for i, l in enumerate(lines):
    fewest_red = 0
    fewest_green = 0
    fewest_blue = 0
    m = r_game.match(l)
    if not m:
        raise Exception(f"Line {i} is not a game")
    print(f"Game {m.group(1)}: {m.group(2)}")
    ID = m.group(1)
    draws = m.group(2).split(";")
    for j, draw in enumerate(draws):
        print(f" draw: {j}")
        for m in r_draw.finditer(draw):
            print(m.groupdict())
            result = m.groupdict()
            if result["color"] == "red":
                fewest_red = max(fewest_red, int(result["cubes"]))
            elif result["color"] == "green":
                fewest_green = max(fewest_green, int(result["cubes"]))
            elif result["color"] == "blue":
                fewest_blue = max(fewest_blue, int(result["cubes"]))
    minimum_set_power = fewest_blue * fewest_green * fewest_red
    minimum_powers.append(minimum_set_power)

print("Sum of minimum set powers: {}".format(sum(minimum_powers)))
