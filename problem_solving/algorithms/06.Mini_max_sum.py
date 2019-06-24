#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    min_sum = 0
    max_sum = 0
    for i in range(0, 4):
        min_sum += arr[i]
    for i in range(1, 5):
        max_sum += arr[i]
    print(str(min_sum) + " " + str(max_sum))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
