
import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.


def countApplesAndOranges(s, t, a, b, apples, oranges):
    left_tree_to_left_house_side_distance = s - a
    left_tree_to_right_house_side_distance = t - a

    right_tree_to_left_house_side_distance = t - b
    right_tree_to_right_house_side_distance = s - b

    apples_in_range = 0
    oranges_in_range = 0
    for apple in apples:
        if apple >= left_tree_to_left_house_side_distance and left_tree_to_right_house_side_distance >= apple:
            apples_in_range += 1
    for orange in oranges:
        if orange <= right_tree_to_left_house_side_distance and right_tree_to_right_house_side_distance <= orange:
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
