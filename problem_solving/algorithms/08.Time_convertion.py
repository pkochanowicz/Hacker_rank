#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    s = s.split(":")

    if s[-1][-2:] == "PM":
        if s[0] == "12":
            s[0] = "00"
        s[-1] = s[-1].replace("PM", "")
        s[0] = str(int(s[0]) + 12)
    if s[-1][-2:] == "AM":
        if s[0] == "12":
            s[0] = "00"
        s[-1] = s[-1].replace("AM", "")

    s = ":".join(s)

    return s

if __name__ == '__main__':
    s = input()

    result = timeConversion(s)

    print(result)