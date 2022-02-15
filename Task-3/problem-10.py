# https://www.hackerrank.com/challenges/drawing-book/problem
# Drawing Book
# How many pages does a student need to turn to get to page p?


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    return min((p - p % 2)//2, ((n  - n % 2) - (p - p % 2))//2);
    '''
    m = n
    f = p + (1- p % 2);
    m = min(int((f - 1)/2), m);
    f = p + n % 2 - p % 2;
    m = min(int((n - f)/2), m);
    return m;
    '''
    
if __name__ == '__main__':
#   #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    print(str(result));
#   #fptr.write(str(result) + '\n')

#   #fptr.close()



'''
Sample Input 0:
6
2

Sample Output 0:
1

'''
