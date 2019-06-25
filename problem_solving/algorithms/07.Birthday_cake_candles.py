#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.


def birthdayCakeCandles(ar):
    highest_count = 0
    highest_height = 0
    for i in ar:
        if i > highest_height:
            highest_height = i
            highest_count = 1
        elif i == highest_height:
            highest_count += 1
    return highest_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    print(str(result))
