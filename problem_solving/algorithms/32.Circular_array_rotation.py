#!/bin/python3

import math
import os
import random
import re
import sys

from collections import deque

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    a = deque(a)
    a.rotate(k)
    a = list(a)
    result = []
    for q in queries:
        result.append(a[q])
    return result


if __name__ == '__main__':
    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    print(result)