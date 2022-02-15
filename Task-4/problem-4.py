# https://www.hackerrank.com/challenges/library-fine/problem
# Library Fine
# Help your library calculate fees for late books!

#import math
#import os
#import random
#import re
#import sys

#
# Complete the 'libraryFine' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2
#

def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    if(y2 * 32 * 13 + m2 * 32 + d2 > y1 * 32 * 13 + m1 * 32 + d1):
        return 0;
    elif (y2 < y1):
        return 10000;
    elif (m2 < m1):
        return (m1 - m2) * 500;
    else:
        return (d1 - d2) * 15;

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    d1 = int(first_multiple_input[0])

    m1 = int(first_multiple_input[1])

    y1 = int(first_multiple_input[2])

    second_multiple_input = input().rstrip().split()

    d2 = int(second_multiple_input[0])

    m2 = int(second_multiple_input[1])

    y2 = int(second_multiple_input[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    print(str(result));
    #fptr.write(str(result) + '\n')

    #fptr.close()

'''
Sample Input:
9 6 2015
6 6 2015

Sample Output:
45

'''
