#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    level_count = 0
    valleys_count = 0
    for step in s:
        is_in_valley = level_count < 0
        if step == "U":
            level_count += 1
        if step == "D":
            level_count -= 1
        if is_in_valley:
            has_exited_valley = level_count >= 0
            if has_exited_valley:
                valleys_count += 1
    return valleys_count


if __name__ == '__main__':
    n = int(input())

    s = input()

    result = countingValleys(n, s)

    print(result)