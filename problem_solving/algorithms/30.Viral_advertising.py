import math
import os
import random
import re
import sys
import math

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    likes = 0
    for i in range(1, n+1):
        if i == 1:
            likes += 2
        elif i > 1:
            if 'new_likes' in locals():
                new_likes = math.floor((new_likes * 3)/2)
            else:
                new_likes = math.floor((likes * 3) / 2)
            likes += new_likes
    return likes


if __name__ == '__main__':
    n = int(input())

    result = viralAdvertising(n)

    print(result)
