#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    last_prisoner = m % n + (s - 1)
    if n == m:
        last_prisoner = n + (s - 1)
    if last_prisoner > n:
        last_prisoner = last_prisoner % n
    if last_prisoner == 0:
        last_prisoner = n
    return last_prisoner


    # current_prisoner = s
    # for i in range(1, m):
    #     if current_prisoner >= n:
    #         current_prisoner = 1
    #     else:
    #         current_prisoner += 1
    # return current_prisoner


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)

        print(result)
