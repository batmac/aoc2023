#!/usr/bin/env python3

import re
import sys

from tqdm import tqdm

if len(sys.argv) != 2:
    print("Usage: {} <filename>".format(sys.argv[0]))
    sys.exit(1)


#####
def run(fh):
    times = [int(x) for x in re.findall(r"\d+", fh.readline().replace(" ", ""))]
    distances = [int(x) for x in re.findall(r"\d+", fh.readline().replace(" ", ""))]
    print(f"times: {times} , distances: {distances}")

    answer = 1
    for t, d in zip(times, distances):
        print(f"t: {t}, d: {d}")
        win = 0
        for hold_time in tqdm(range(t + 1)):
            distance = hold_time * (t - hold_time)
            # print(f"hold_time: {hold_time} , distance: {distance}")
            if distance > d:
                win += 1
        # print(f"win: {win}")
        answer *= win
    print(f"answer: {answer}")


if __name__ == "__main__":
    with open(sys.argv[1]) as fh:
        run(fh)
