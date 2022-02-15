# https://www.hackerrank.com/challenges/kangaroo/problem
# Number Line Jumps
# Can two kangaroo meet after making the same number of jumps?


##import math
##import os
##import random
##import re
##import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if(v1 == v2):
        if(x1 == x2):
            return "YES";
        else:
            return "NO";
    elif(((x2-x1)/(v1-v2) >= 1) and ((x2-x1)%(v1-v2) == 0)):
        return "YES";
    else:
        return "NO";
    
if __name__ == '__main__':
#    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

#    #fptr.write(result + '\n')
    print(result);
#    #fptr.close()


'''
Sample Input 0
0 3 4 2

Sample Output 0
YES


Sample Input 1
0 2 5 3

Sample Output 1
NO


x1 + n*v1 = x2 + n*v2  at jump number n
so
n = (x2-x1)/(v1-v2) then n should be integer(not double or float) greater than or equal to 1 or v1 is equal to v2 and x1 is equal to x2 
'''
