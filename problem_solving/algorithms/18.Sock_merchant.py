#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    print(ar)
    pair_count = 0
    i = 0
    while i < len(ar)-1:
        if ar[i] == ar[i+1]:
            pair_count += 1
            i += 2
        else:
            i += 1
    return pair_count


if __name__ == '__main__':
    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
