# https://www.hackerrank.com/challenges/electronics-shop/problem 
# Electronics Shop
# Determine the most expensive Keyboard and USB drive combination one can purchase within her budget.

#import os
#import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    available = -1;
    keyboards.sort();
    drives.sort();
    for i in keyboards:
        for j in drives:
            if i + j <= b:
                availble = max(i + j, available);
            else:
                break;
    return available

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    print(str(moneySpent));
    #fptr.write(str(moneySpent) + '\n')

    #fptr.close()


'''
Sample Input 0:
10 2 3
3 1
5 2 8

Sample Output 0:
9

''
Sample Input 1:
5 1 1
4
5

Sample Output 1:
-1

'''
