#!/usr/bin/env python3

import re
import sys

if len(sys.argv) != 2:
    print("Usage: {} <filename>".format(sys.argv[0]))
    sys.exit(1)


#####


def split_srcONErange_to_disjoint_ranges_by_destranges(srcrange, destranges):
    # destranges must be sorted
    # print(f"split_srcONErange_to_disjoint_ranges_by_destranges({srcrange}, {destranges})")
    smin = srcrange[0]
    smax = srcrange[1]
    disjoint_ranges = []

    for destrange in destranges:
        if smax <= destrange[0]:
            return disjoint_ranges + [(smin, smax)]
        elif smin >= destrange[1]:
            continue
        elif smin >= destrange[0] and smax <= destrange[1]:
            return disjoint_ranges + [(smin, smax)]
        elif smin >= destrange[0] and smax > destrange[1]:
            disjoint_ranges.append((smin, destrange[1]))
            smin = destrange[1]
            continue
        elif smin < destrange[0]:
            disjoint_ranges.append((smin, destrange[0]))
            smin = destrange[0]
            continue
    else:
        disjoint_ranges.append((smin, smax))

    return disjoint_ranges


def split_srcranges_to_disjoint_ranges_by_destranges(srcranges, destranges):
    print(" split ranges {} {}".format(srcranges, destranges))
    disjoint_ranges = []
    for srcrange in srcranges:
        disjoint_ranges += split_srcONErange_to_disjoint_ranges_by_destranges(
            srcrange, destranges
        )
    print(" disjointed_ranges  -> {}".format(disjoint_ranges))
    return disjoint_ranges


def run(fh):
    s = [int(x) for x in fh.readline().split(":")[1].split()]
    seedranges = [(s, s + l) for s, l in zip(s[::2], s[1::2])]
    # seedranges.sort(key=lambda x: x[0])
    print(f"seedranges: {seedranges}")

    sep = re.compile(r"\n\n")
    blocks = sep.split(fh.read())

    luts = {}
    for block in blocks:
        block = list(filter(None, block.splitlines()))
        lut = []
        for line in block[1:]:
            dest, source, length = line.split()
            lut.append(
                (
                    (int(source), int(source) + int(length)),
                    (int(dest), int(dest) + int(length)),
                )
            )
        lut.sort(key=lambda x: x[0])
        luts[block[0]] = lut

    ranges = seedranges
    for m, lut in luts.items():
        print(f"next, ranges: {ranges}")
        for entry in lut:
            print(f"  lut {m}: {entry[0]} -> {entry[1]}")
        ranges = split_srcranges_to_disjoint_ranges_by_destranges(
            ranges, [t[0] for t in lut]
        )
        checked_ranges = []
        # convert ranges
        for range in ranges:
            newrange = range
            for entry in lut:
                if range[0] >= entry[0][0] and range[1] <= entry[0][1]:
                    print(
                        f" range must be converted: {range} ({entry[0]} -> {entry[1]})"
                    )
                    newrange = (
                        range[0] + entry[1][0] - entry[0][0],
                        range[1] + entry[1][0] - entry[0][0],
                    )
                    print(f" range converted: {newrange}")
                    # checked_ranges.append(newrange)
                    break

            checked_ranges.append(newrange)

        print(f"converted ranges: {checked_ranges}")
        ranges = checked_ranges
    print(f"final ranges: {checked_ranges}")
    checked_ranges.sort(key=lambda x: x[0])
    print(f"minimum location: {checked_ranges[0][0]}")


if __name__ == "__main__":
    with open(sys.argv[1]) as fh:
        run(fh)
