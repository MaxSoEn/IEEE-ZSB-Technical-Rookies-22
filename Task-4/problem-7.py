# https://www.hackerrank.com/challenges/kaprekar-numbers/problem
# Modified Kaprekar Numbers
# Print kaprekar numbers in the given range

#import math
#import os
#import random
#import re
#import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    # Write your code here
    c = 0;
    for i in range(p,q + 1):
        s = str(i**2);
        if(i == int(s[0:len(s) - len(str(i))].zfill(1))+int(s[len(s)-len(str(i)):].zfill(1))):
            print(i, end=' ');
            c += 1;
    if c == 0 :
        print("INVALID RANGE");

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
'''
Sample Input:
STDIN   Function
-----   --------
1       p = 1
100     q = 100

Sample Output:
1 9 45 55 99


'''
