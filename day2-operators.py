#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * (tip_percent / 100.0)
    tax = meal_cost * (tax_percent / 100.0)
    print(int(round(meal_cost + tip + tax)))

solve(12.00, 20, 8) == 15