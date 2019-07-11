#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    i = 0
    front_count = 0
    back_count = 0
    if p == 1 or (p == n and n % 2 == 0):
        return min(front_count, back_count)
    while n > i:
        if i == p or i+1 == p:
            break
        else:
            i += 2
            front_count += 1
        if i >= n:
            break
    i = n
    while i > 0:
        if n % 2 == 0:
            if i == p or i+1 == p:
                break
        else:
            if i == p or i-1 == p:
                break
        i -= 2
        back_count += 1
        if i <= 0:
            break
    return min(front_count, back_count)


if __name__ == '__main__':
    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    print(result)