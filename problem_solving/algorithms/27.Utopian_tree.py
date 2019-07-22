#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    tree_height = 1
    for i in range(1, n+1):
        if i % 2 == 0:
            tree_height += 1
        elif i % 2 == 1:
            tree_height *= 2
    return tree_height


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        print(result)