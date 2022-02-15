#https://www.hackerrank.com/challenges/between-two-sets/problem
#Between Two Sets
#Find the number of integers that satisfies certain criteria relative to two sets.

##import math
##import os
##import random
##import re
##import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    x = 0;                              # conditional variable 0 is a number isn't vaild and 1 if it's vaild
    l = [];                             # list of the vaild number
    for i in range(max(a), min(b) + 1): # loop start to check from biggest number in list 1 to smallest number in list 2
        for n in a:                     # loop on each element on first array
            if(i % n == 0):             # if the elements of the first array are all factors of the current number
                x = 1;                  # number is still vaild
            else:                       # if one of the elements of the first array is not factor of the number
                x = 0;                  # number is not vaild
                break;                  # no need to continue
        n = 0;                          # n is a counter to start from first element in array b
        while(x == 1 and n < len(b)):   # loop to check the second condition of the vaildation of the number(break if it end or its not vaild)
            if(b[n] % i == 0):          # if the current number is a factor of all elements in second array
                x = 1;                  # number is still vaild
            else:                       # if the current number is not a factor of one element of second array
                x = 0;                  # number is not vaild
            n += 1;                     # check next element
        if(x == 1):                     # if number is vaild for all conditions
            l.append(i);                # add it to list
    return len(l);                      # return the count of the vaild numbers

if __name__ == '__main__':
#    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

#    #fptr.write(str(total) + '\n')

#    #fptr.close()

    print(total);

'''
Sample Input
2 3
2 4
16 32 96

Sample Output
3

Explanation
2 and 4 divide evenly into 4, 8, 12 and 16.
4, 8 and 16 divide evenly into 16, 32, 96.

4, 8 and 16 are the only three numbers for which each element of a is a factor and each is a factor of all elements of b.

'''
