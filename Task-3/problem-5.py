# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
# Breaking the Records
# Given an array of Maria's basketball scores all season, determine the number of times she breaks her best and worst records.


#import math
#import os
#import random
#import re
#import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    min_score = scores[0];
    max_score = scores[0];
    result = [0, 0];
    for i in scores:
        if(min_score > i):
            result[1] += 1;
            min_score = i;
        if(max_score < i):
            result[0] += 1;
            max_score = i;
    return result; 
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(' '.join(map(str, result)));
    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
'''
Sample Input 0:
9
10 5 20 20 4 5 2 25 1

Sample Output 0:
2 4

'''
