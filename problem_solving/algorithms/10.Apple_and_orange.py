
import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.


def countApplesAndOranges(s, t, a, b, apples, oranges):
    distance_from_apple_tree = s - a
    distance_from_orange_tree = t - b
    distance_from_apple_tree2 = t - a
    distance_from_orange_tree2 = s - b
    apples_in_range = 0
    oranges_in_range = 0
    for apple in apples:
        if apple >= distance_from_apple_tree and distance_from_apple_tree2 >= apple:
            apples_in_range += 1
    for orange in oranges:
        if orange <= distance_from_orange_tree and distance_from_orange_tree2 <= orange:
            oranges_in_range += 1
    print(apples_in_range)
    print(oranges_in_range)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
