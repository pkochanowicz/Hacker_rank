#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    highest_score, lowest_score = scores[0], scores[0]
    highest_score_count = 0
    lowest_score_count = 0
    for score in scores:
        if score > highest_score:
            highest_score_count += 1
            highest_score = score
        elif score < lowest_score:
            lowest_score_count += 1
            lowest_score = score
    return highest_score_count, lowest_score_count


if __name__ == '__main__':
    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(result)
