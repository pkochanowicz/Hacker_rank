#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    for i in range(4):
        for j in range(4):
            current_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] +                             arr[i+2][j+1] + arr[i+2][j+2]
            if i == 0 and j == 0:
                max_sum = current_sum
            if current_sum > max_sum:
                max_sum = current_sum
            j += 1
        i += 1
    return max_sum



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
