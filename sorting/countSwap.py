#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#


def countSwaps(a):
    # Write your code here
    cnt = 0
    for i in range(len(a)):  # loop through each element in the array a
        for j in range(i + 1,
                       len(a)):  # loop through the array a start from i + 1
            if a[i] > a[
                    j]:  # if the values of a[i] greator than it's right adjcent element swap them
                a[i], a[j] = a[j], a[i]
                cnt += 1  # count the number of swap
    print('Array is sorted in {} swaps.'.format(cnt))
    print('First Element: {}'.format(a[0]))
    print('Last Element: {}'.format(a[-1]))

    if __name__ == '__main__':
        n = int(input().strip())
        a = list(map(int, input().rstrip().split()))
        countSwaps(a)
