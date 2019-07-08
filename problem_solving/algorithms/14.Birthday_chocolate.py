#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    portion_possibilities = 0
    for index, square in enumerate(s):
        squares_count = 0
        square_sum = 0
        while squares_count < m:
            square_sum += s[index + squares_count]
            squares_count += 1
        if square_sum == d:
            portion_possibilities += 1
        if index + squares_count == len(s):
            break
    return portion_possibilities


if __name__ == '__main__':
    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    print(result)
