#!/usr/bin/env python3

import re
import sys

if len(sys.argv) != 2:
    print("Usage: {} <filename>".format(sys.argv[0]))
    sys.exit(1)

with open(sys.argv[1], "r") as f:
    lines = f.read().splitlines()


max_red = 12
max_green = 13
max_blue = 14
r_game = re.compile(r"^Game (\d+):(.*)$")
r_draw = re.compile(r"(?: (?P<cubes>\d+) (?P<color>blue|red|green))+")

possible_games = []
for i, l in enumerate(lines):
    m = r_game.match(l)
    if not m:
        raise Exception(f"Line {i} is not a game")
    print(f"Game {m.group(1)}: {m.group(2)}")
    ID = m.group(1)
    draws = m.group(2).split(";")
    still_possible = True
    for j, draw in enumerate(draws):
        print(f" draw: {j}")
        if not still_possible:
            break
        for m in r_draw.finditer(draw):
            # if not m:
            # raise Exception(f"Line {i} is not a draw")
            print(m.groupdict())
            result = m.groupdict()
            if result["color"] == "red" and int(result["cubes"]) > max_red:
                print(f"Game {ID} has more than {max_red} red cubes")
                still_possible = False
                break
            elif result["color"] == "green" and int(result["cubes"]) > max_green:
                print(f"Game {ID} has more than {max_green} green cubes")
                still_possible = False
                break
            elif result["color"] == "blue" and int(result["cubes"]) > max_blue:
                print(f"Game {ID} has more than {max_blue} blue cubes")
                still_possible = False
                break
    # games.append((int(m.group(1)), m.group(2)))
    if still_possible:
        possible_games.append(int(ID))

print(f"Possible games: {possible_games}")
print(f"Sum: {sum(possible_games)}")
