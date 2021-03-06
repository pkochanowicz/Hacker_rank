#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    scores = []
    a_score = 0
    b_score = 0
    for i in range (3):
        if a[i] > b[i]:
            a_score += 1
        elif a[i] < b[i]:
            b_score += 1
    scores.append(a_score)
    scores.append(b_score)
    return scores


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    print(result)
    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()
