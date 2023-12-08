#!/usr/bin/env python3
import re
import sys
from math import lcm

if len(sys.argv) != 2:
    print("Usage: {} <filename>".format(sys.argv[0]))
    sys.exit(1)


#####


def run(fh):
    path = fh.readline().strip()

    fh.readline()
    map = {}
    regex = re.compile(r"(\w+) = \((\w+), (\w+)\)")
    for m in regex.findall(fh.read()):
        a, b, c = m
        # print(f"{a} -> {b} {c}")
        map[a] = (b, c)
    # print(f"map: {map}")

    starts = []
    for key in map.keys():
        if key.endswith("A"):
            starts.append((key, 0))

    print(f"starts: {starts}")

    def find_Z(where: str, path: str):
        steps = 0
        while True:
            for c in path:
                # print(f"direction: {c}")
                steps += 1
                if c == "L":
                    where = map[where][0]
                elif c == "R":
                    where = map[where][1]
                else:
                    raise (f"unknown step: {c}")
                if where.endswith("Z"):
                    return (where, steps)

    allsteps = [find_Z(start[0], path) for start in starts]
    print(f"first steps: {allsteps}")
    all2steps = [find_Z(steps[0], path) for steps in allsteps]
    print(f"loops      : {all2steps}")

    assert allsteps == all2steps  # don't really understand why this is true, but it is

    print(f"lcm: {lcm(*[steps[1] for steps in allsteps])}")


if __name__ == "__main__":
    with open(sys.argv[1]) as fh:
        run(fh)
