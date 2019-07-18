#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    most_expansive_price = 0
    for keyboard in keyboards:
        for drive in drives:
            set_price = keyboard + drive
            if set_price <= b and set_price > most_expansive_price:
                most_expansive_price = set_price
    if most_expansive_price == 0:
        return -1
    else:
        return most_expansive_price

if __name__ == '__main__':
    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    print(moneySpent)
