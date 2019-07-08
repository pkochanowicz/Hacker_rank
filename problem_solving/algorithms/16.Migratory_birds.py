#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    spotted_birds = []
    count = [0, 0, 0, 0, 0, 0]
    most_frequent_bird = 0
    for i in arr:
        spotted_birds.append(i)
    for i in range (1, 6):
        for j in spotted_birds:
            if i == j:
                count[i] += 1
    highest_bird_count = 0
    for i in range (1, 6):
        if count[i] > count[i-1] and count[i] > highest_bird_count:
            most_frequent_bird = i
            highest_bird_count = count[i]
    return most_frequent_bird


if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(result)
