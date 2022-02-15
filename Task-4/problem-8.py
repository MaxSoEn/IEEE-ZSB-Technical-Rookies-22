# https://www.hackerrank.com/challenges/manasa-and-stones/problem
# Manasa and Stones
# Calculate the possible values of the last stone where consecutive values on the stones differ by a value 'a' or a value 'b'.

#import math
#import os
#mport random
#import re
#import sys

#
# Complete the 'stones' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER a
#  3. INTEGER b
#

def stones(n, a, b):
    # Write your code here
    s = [];
    for i in range(n):
        s.append(a * (n - 1 - i) + b * (i));
    return sorted(set(s)); #sort list in ascending order and avoid duplication

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        a = int(input().strip())

        b = int(input().strip())

        result = stones(n, a, b)
        
        print(' '.join(map(str, result)));
        #fptr.write(' '.join(map(str, result)))
        #fptr.write('\n')

    #fptr.close()

'''
Sample Input:
STDIN   Function
-----   --------
2       T = 2 (test cases)
3       n = 3 (test case 1)
1       a = 1
2       b = 2
4       n = 4 (test case 2)
10      a = 10
100     b = 100

Sample Output:
2 3 4 
30 120 210 300

Explanation:
0 * 1 + a*(n - 1 - i) + b*(i)
0 * 1 + 1*(3 - 1 - 0) + 2*(0) = 2
0 * 1 + 1*(3 - 1 - 1) + b*(1) = 3
0 * 1 + 1*(3 - 1 - 2) + b*(2) = 4


10*(4-1-0) + 100*(0) = 30
10*(4-1-1) + 100*(1) = 120
10*(4-1-2) + 100*(2) = 210
10*(4-1-3) + 100*(3) = 300
'''
