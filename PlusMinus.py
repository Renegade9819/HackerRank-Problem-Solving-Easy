#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive = 0
    negative = 0
    zeros = 0

    length = len(arr)

    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zeros +=1

    a = positive / length
    print(round(a, 6))
    b = negative / length
    print(round(b, 6))
    c = zeros / length
    print(round(c, 6))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
