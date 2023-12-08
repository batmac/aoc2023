#!/usr/bin/env python3
import re
import sys

if len(sys.argv) != 2:
    print("Usage: {} <filename>".format(sys.argv[0]))
    sys.exit(1)


#####


def run(fh):
    path = fh.readline().strip()

    fh.readline()
    map = {}
    regex = re.compile(r"([A-Z]+) = \(([A-Z]+), ([A-Z]+)\)")
    for m in regex.findall(fh.read()):
        a, b, c = m
        print(f"{a} -> {b} {c}")
        map[a] = (b, c)
    # print(f"map: {map}")

    steps = 0
    where = "AAA"
    while where != "ZZZ":
        for c in path:
            # print(f"direction: {c}")
            steps += 1
            if c == "L":
                where = map[where][0]
            elif c == "R":
                where = map[where][1]
            else:
                raise (f"unknown step: {c}")
            print(f"{where}", end=" ")
            if where == "ZZZ":
                print(f"found exit after {steps} steps")
                break
        else:
            print(f"no exit found after {steps} steps, restarting the directions")


if __name__ == "__main__":
    with open(sys.argv[1]) as fh:
        run(fh)
