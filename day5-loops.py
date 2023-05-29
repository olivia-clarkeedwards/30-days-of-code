#!/bin/python3

import math
import os
import random
import re
import sys

def printFirstTenMultiples(n):
    
    for i in range(1, 11):
        multiple = i * n 
        print(f'{n} x {i} = {multiple}')
    

if __name__ == '__main__':
    n = int(input().strip())
    printFirstTenMultiples(n)
