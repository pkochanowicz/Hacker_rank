#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    distance_one = int(math.fabs(x-z))
    distance_two = int(math.fabs(y-z))
    if distance_one < distance_two:
        return "Cat A"
    elif distance_one > distance_two:
        return "Cat B"
    else:
        return "Mouse C"


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        print(result + '\n')
