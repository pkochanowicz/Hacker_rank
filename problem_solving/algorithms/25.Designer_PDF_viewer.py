#!/bin/python3

import math
import os
import random
import re
import sys
import string
# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    alphabet = string.ascii_lowercase
    highest_letter = 0

    for i in word:
        for index, j in enumerate(alphabet):
            if i == j and h[index] > highest_letter:
                highest_letter = h[index]
                continue

    number_of_letters = len(word)
    print(highest_letter, number_of_letters)
    return highest_letter * number_of_letters


if __name__ == '__main__':
    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    print(result)