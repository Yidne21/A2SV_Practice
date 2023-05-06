#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def countingSort(arr):
    # Write your code here
    freqArr = [0] * 100
    sortedArr = []
    for i in arr: # loop through each elements of the array
        if freqArr[i] == 0: # check the element freq in the freqArray
            cnt = arr.count(i) # count the occurence of each element
            freqArr[i] = cnt # store the occurence in freqArray at the element i postion
    for i in range(len(freqArr)): # loop the freqArr
        if freqArr[i] != 0: # check if the value is not equal zero at i postion
            for _ in range(freqArr[i]): # loop as value of freqArr[i] times
                sortedArr.append(i) # append the index i which is the  value of the unsorted array in to a sorted array
    sortedArr = ' '.join(map(int, sortedArr))
    return sortedArr


if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)
    print(result)
