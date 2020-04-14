#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice_score = 0
    bob_score = 0

    for (i, j) in zip(a, b):
        if i > j:
            alice_score += 1
        elif i == j:
            alice_score += 0
            bob_score += 0
        else:
            bob_score += 1
    
    scores = [0, 0]
    scores[0] = alice_score
    scores[1] = bob_score
    
    return scores


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
