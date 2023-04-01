#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    splitter = ":"
    arr = s.split(splitter)
    test = arr[-1]
    if(test[-2:] == "PM" and int(arr[0])<12):
        a = int(arr[0]) + 12
        arr[0] = str(a)
    elif(test[-2:] == "AM" and int(arr[0]) == 12):
        arr[0]="00"
    arr[-1] = arr[-1][0:2]
    print(splitter.join(arr))

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)
