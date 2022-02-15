# https://www.hackerrank.com/challenges/find-digits/problem
# Find Digits
# Calculate the number of digits in an integer that evenly divide it.

#import math
#import os
#import random
#import re
#import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    # Write your code here
    num = int(n);
    count = 0;
    while(num != 0):
        if(num % 10 == 0):
            num = num // 10;
            continue;
        if(n % (num % 10) == 0):
            count += 1;
        num = num // 10;
    return count;
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)
        
        print(str(result));
        #fptr.write(str(result) + '\n')

    #fptr.close()


'''
Sample Input:
2
12
1012

Sample Output:
2
3

'''
