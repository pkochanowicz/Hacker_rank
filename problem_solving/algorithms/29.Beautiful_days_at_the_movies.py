#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    number_of_beautiful_days = 0
    for day in range(i, j+1):
        reversed_day = int(str(day)[::-1])
        if math.fabs(day-reversed_day)%k == 0:
            number_of_beautiful_days += 1
        print(day)
    return number_of_beautiful_days


if __name__ == '__main__':
    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    print(result)
