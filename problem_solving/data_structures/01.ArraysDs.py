import os
import random
import re
import sys

# Complete the reverseArray function below.

def reverseArray(a):
    print(a)
    b = str(a).replace("[", "").replace("]", "").replace(",", "").split()
    return b[::-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()