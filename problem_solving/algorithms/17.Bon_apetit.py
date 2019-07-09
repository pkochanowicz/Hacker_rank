#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.


def bonAppetit(bill, k, b):
    price_total = sum(bill)/2
    price_anna = price_total - bill[k]/2
    if price_anna == b:
        print("Bon Appetit")
    else:
        print(int(b-price_anna))


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
