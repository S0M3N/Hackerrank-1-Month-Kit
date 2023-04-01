#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    primary_sum = 0
    secondary_sum = 0
    n = len(arr)
    for i in range(n):
        primary_sum += arr[i][i]
        secondary_sum += arr[i][n-i-1]

    # return the absolute difference between the sums
    res = abs(primary_sum - secondary_sum)
    print(res)

if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
