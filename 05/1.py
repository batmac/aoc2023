#!/usr/bin/env python3

import re
import sys

if len(sys.argv) != 2:
    print("Usage: {} <filename>".format(sys.argv[0]))
    sys.exit(1)


#####


def run(fh):
    seeds = [int(x) for x in fh.readline().split(":")[1].split()]
    assert len(seeds) != 0

    sep = re.compile(r"\n\n")
    blocks = sep.split(fh.read())

    luts = {}
    for block in blocks:
        block = list(filter(None, block.splitlines()))
        # print(f"block: {block!r}")
        lut = []
        for line in block[1:]:
            dest, source, length = line.split()
            lut.append(
                {"dest": int(dest), "source": int(source), "length": int(length)}
            )
        luts[block[0]] = lut
    for lut, v in luts.items():
        print(f"{lut}: {v}")
    soils = []
    for seed in seeds:
        print(f"seed {seed}:")
        mapped = seed
        for name, lut in luts.items():
            for entry in lut:
                if (
                    mapped >= entry["source"]
                    and mapped < entry["source"] + entry["length"]
                ):
                    mapped = entry["dest"] + (mapped - entry["source"])
                    break
            print(f"  {name}: {mapped}")
        soils.append(mapped)
    print(f"closest soil: {min(soils)}")


if __name__ == "__main__":
    with open(sys.argv[1]) as fh:
        run(fh)
