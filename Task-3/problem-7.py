# https://www.hackerrank.com/challenges/migratory-birds/problem
# Migratory Birds
# Determine which type of bird in a flock occurs at the highest frequency.

#import math
#import os
#import random
#import re
#import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    t = [0, 0, 0, 0, 0];
    for i in arr:
        t[i - 1] += 1;
    
    max_num = 0;
    for i in range(len(t)):
        if max_num < t[i]:
            index = i;
            max_num = t[i];
    return index + 1;
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)
    
    print(str(result));
    #fptr.write(str(result) + '\n')

    #fptr.close()
'''
Sample Input 0:
6
1 4 4 4 5 3

Sample Output 0:
4

'''
