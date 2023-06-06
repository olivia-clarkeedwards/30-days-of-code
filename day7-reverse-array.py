#!/bin/python3

import math
import os
import random
import re
import sys


def printReversedArray(arr):
    
    for i in range(len(arr) - 1, -1, -1):
        print(arr[i], end=" ")


n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
printReversedArray(arr)