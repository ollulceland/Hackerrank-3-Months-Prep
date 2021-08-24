#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'plusMinus' function below.
# The function accepts INTEGER_ARRAY arr as parameter.

def plusMinus(arr):
    positive_counter = 0
    negative_counter = 0
    zero_counter = 0
    
    for i in range(len(arr)):
        if arr[i] > 0:
            positive_counter += 1
        elif arr[i] < 0:
            negative_counter += 1
        else:
            zero_counter += 1
    print("%f"%(positive_counter/len(arr)))
    print("%f"%(negative_counter/len(arr)))
    print("%f"%(zero_counter/len(arr))) 

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
