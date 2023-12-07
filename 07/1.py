#!/usr/bin/env python3

import re
import sys
from enum import Enum
from functools import cmp_to_key

from tqdm import tqdm

if len(sys.argv) != 2:
    print("Usage: {} <filename>".format(sys.argv[0]))
    sys.exit(1)


#####
# define hand types as sortable consts
#####


class HandType(Enum):
    FIVE_OF_A_KIND = 0
    FOUR_OF_A_KIND = 1
    FULL_HOUSE = 2
    THREE_OF_A_KIND = 3
    TWO_PAIR = 4
    ONE_PAIR = 5
    HIGH_CARD = 6


def run(fh):
    hands = [line.split() for line in fh]

    print(f"Hands: {hands}")

    hands = [(hand[0], hand[1], hand_type(hand[0])) for hand in hands]
    for hand in hands:
        print(f"Hand: {hand}")

    hands_sorted = sorted(hands, key=cmp_to_key(hand_compare))
    # print(f"Sorted: {sorted(hands,key=cmp_to_key(hand_compare))}")

    total_sum = sum((i + 1) * int(hand[1]) for i, hand in enumerate(hands_sorted))
    print(f"Sum: {total_sum}")


def hand_compare(th1, th2):
    h1, h2 = th1[0], th2[0]
    v1, v2 = th1[2].value, th2[2].value
    assert h1 != h2, "Hands are the same"
    if v1 > v2:
        return -1
    elif v1 < v2:
        return 1
    else:
        card_order = "AKQJT98765432"
        for c in range(5):
            if card_order.index(h1[c]) > card_order.index(h2[c]):
                return -1
            elif card_order.index(h1[c]) < card_order.index(h2[c]):
                return 1


def hand_type(hand):
    hand = sorted(hand)
    if five_of_a_kind(hand):
        return HandType.FIVE_OF_A_KIND
    elif four_of_a_kind(hand):
        return HandType.FOUR_OF_A_KIND
    elif full_house(hand):
        return HandType.FULL_HOUSE
    elif three_of_a_kind(hand):
        return HandType.THREE_OF_A_KIND
    elif two_pair(hand):
        return HandType.TWO_PAIR
    elif one_pair(hand):
        return HandType.ONE_PAIR
    elif high_card(hand):
        return HandType.HIGH_CARD


# all these functions assume the hand is sorted and are called in order of precedence of hand types
def five_of_a_kind(h):
    return len(set(h)) == 1


def four_of_a_kind(h):
    return (h[0] == h[1] == h[2] == h[3]) or (h[1] == h[2] == h[3] == h[4])


def full_house(h):
    return (h[0] == h[1] == h[2] and h[3] == h[4]) or (
        h[0] == h[1] and h[2] == h[3] == h[4]
    )


def three_of_a_kind(h):
    return (h[0] == h[1] == h[2]) or (h[1] == h[2] == h[3]) or (h[2] == h[3] == h[4])


def two_pair(h):
    return (
        (h[0] == h[1] and h[2] == h[3])
        or (h[0] == h[1] and h[3] == h[4])
        or (h[1] == h[2] and h[3] == h[4])
    )


def one_pair(h):
    # return (h[0] == h[1]) or (h[1] == h[2]) or (h[2] == h[3]) or (h[3] == h[4])
    return len(set(h)) == 4


def high_card(h):
    return len(set(h)) == 5


if __name__ == "__main__":
    with open(sys.argv[1]) as fh:
        run(fh)
