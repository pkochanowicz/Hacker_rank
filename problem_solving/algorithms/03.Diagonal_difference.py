#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    left_to_right_diagonal = 0
    right_to_left_diagonal = 0
    for i in range (len(arr[0])):
        left_to_right_diagonal += arr[i][i]
        right_to_left_diagonal += arr[i][len(arr[0])-1-i]
    return abs(left_to_right_diagonal-right_to_left_diagonal)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
