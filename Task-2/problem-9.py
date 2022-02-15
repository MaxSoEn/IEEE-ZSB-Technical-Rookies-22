# https://www.hackerrank.com/challenges/diagonal-difference/problem 
# Diagonal Difference
# Calculate the absolute difference of sums across the two diagonals of a square matrix.

##import math   # library to use mathimatical functions
##import os     # to access some fuctions in os
##import random # to create a random value
##import re     # to Regular Expresion search or match
##import sys    # some Expression of system and commands like exit(0) 

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    f = 0;                              # forward diagonal
    b = 0;                              # back diagonal
    for i in range(len(arr)):           # loop for each column 
        f += arr[i][i];                 # Calculate the sum of forward diagonal elements
        b += arr[i][len(arr)- i - 1];   # Calculate the sum of back diagonal elements
    return abs(f-b);                    # Calulate the absolute differance

if __name__ == '__main__':
#    #fptr = open(os.environ['OUTPUT_PATH'], 'w');      # create file to save the result

    n = int(input().strip());                                   # size of array is n*n

    arr = [];                                                   # 2D array

    for _ in range(n):                                          # loop for each column
        arr.append(list(map(int, input().rstrip().split())));   # Add each line as a nested list

    result = diagonalDifference(arr);                           # Call function and store result of its return

    print(result);                                              # print the result
#    #fptr.write(str(result) + '\n');                   # save result as a string

#    #fptr.close();                                     # close the file

'''
Sample Input
3
11 2 4
4 5 6
10 8 -12

Sample Output
15

Explanation
The primary diagonal is:
11
   5
     -12
     
Sum across the primary diagonal: 11 + 5 - 12 = 4

The secondary diagonal is:
     4
   5
10

Sum across the secondary diagonal: 4 + 5 + 10 = 19

Difference: |4 - 19| = 15

Note: |x| is the absolute value of x
'''
