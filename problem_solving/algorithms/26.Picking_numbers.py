#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    result_array = []
    a = sorted(a)
    print(a)
    for index, i in enumerate(a):
        second_index = 0
        result_array.append([])
        max_value, min_value = i, i
        for j in a:
            if math.fabs(min_value - j) <= 1 and math.fabs(max_value - j) <= 1:
                result_array[index].append([])
                result_array[index][second_index] = j
                second_index += 1
                if j > max_value:
                    max_value = j
                if j < min_value:
                    min_value = j
    print(result_array)

    longest_array_length = 0
    for array in result_array:
        if len(array) > longest_array_length:
            longest_array_length = len(array)
    return longest_array_length

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(result)