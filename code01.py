#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    neg = 0
    pos = 0
    zer = 0
    s = len(arr)
    for i in arr:
        if(i<0):
            neg+=1
        elif(i>0):
            pos+=1
        else:
            zer+=1
    print("{:.6f}".format(pos/s))
    print("{:.6f}".format(neg/s))
    print("{:.6f}".format(zer/s))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
