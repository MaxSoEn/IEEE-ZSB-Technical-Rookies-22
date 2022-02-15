# https://www.hackerrank.com/challenges/counting-valleys/problem
# Counting Valleys
# Count the valleys encountered during vacation.


##import math
##import os
##import random
##import re
##import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    ch = 0;
    v = 0;
    m = 0;
    for i in path:
        if(ch == -1 and i == 'U'):
            v += 1;
        elif(ch == +1 and i == 'D'):
            m += 1;
        if(i == 'D'):
            ch -= 1;
        elif(i == 'U'):
            ch += 1;
    return v;

if __name__ == '__main__':
#    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    print(str(result));
#    #fptr.write(str(result) + '\n')

#    #fptr.close()


'''
Sample Input:
8
UDDDUDUU

Sample Output:
1

'''
