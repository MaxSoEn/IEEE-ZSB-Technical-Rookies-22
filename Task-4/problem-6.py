# https://www.hackerrank.com/challenges/chocolate-feast/problem
# Chocolate Feast
# Calculate the number of chocolates that can be bought following the given conditions.

#!/bin/python3

#import math
#import os
#import random
#import re
#import sys

#
# Complete the 'chocolateFeast' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c
#  3. INTEGER m
#

def chocolateFeast(n, c, m):
    # Write your code here
    num = n // c;
    warpper = num // m ;
    reminder = num%m + warpper;
    num += warpper;
    while(reminder >= m):
        warpper = reminder // m ;
        reminder = reminder%m + warpper;
        num += warpper;
    return num;
    
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        c = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        result = chocolateFeast(n, c, m)

        print(str(result));
        #fptr.write(str(result) + '\n')

    #fptr.close()


'''
Sample Input:
STDIN   Function
-----   --------
3       t = 3 (test cases)
10 2 5  n = 10, c = 2, m = 5 (first test case)
12 4 4  n = 12, c = 4, m = 4 (second test case)
6 2 2   n = 6,  c = 2, m = 2 (third test case)

Sample Output:
6
3
5

'''
