#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive_numbers_count = 0
    negative_numbers_count = 0
    zeros_count = 0
    for i in arr:
        if i > 0:
            positive_numbers_count += 1
        elif i < 0:
            negative_numbers_count += 1
        elif i == 0:
            zeros_count += 1
    print(positive_numbers_count/len(arr))
    print(negative_numbers_count/len(arr))
    print(zeros_count/len(arr))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
