#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#


def insertionSort1(n, arr):
    # Write your code here
    isSorted = False
    lastEle = arr[-1]
    for i in range(n - 1, -1, -1):
        if isSorted:
            break
        for j in range(n - 1, -1, -1):
            if lastEle < arr[j - 1] and j != 0:
                arr[j] = arr[j - 1]
                array_string = ' '.join(map(str, arr))
                print(array_string)

            elif lastEle > arr[j - 1] or j == 0:
                arr[j] = lastEle
                array_string = ' '.join(map(str, arr))
                print(array_string)
                isSorted = True
                break


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)