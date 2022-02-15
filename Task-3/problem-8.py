# https://www.hackerrank.com/challenges/sock-merchant/problem
# Sales by Match
# How many pairs of socks can Alex sell?

#import math
#import os
#import random
#import re
#import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    col = []; # list of colors
    num = []; # list of number of socks of each color
    for i in ar:
        if(i in col):
            num[col.index(i)] += 1;
        else:
            col.append(i);
            num.append(1);
    sum = 0;
    for i in num:
        sum += int(i/2);
    return sum;
    
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    
    print(str(result));
    #fptr.write(str(result) + '\n')

    #fptr.close()


'''
Sample Input:
STDIN                       Function
-----                       --------
9                           n = 9
10 20 20 10 10 30 50 10 20  ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

Sample Output:
3

'''
