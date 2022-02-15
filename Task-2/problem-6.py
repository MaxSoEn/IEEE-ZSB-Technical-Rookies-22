# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# this program finds the Runner-Up Score
# for a given list of numbers, it prints the second largest number.

if __name__ == '__main__':
    n = int(input());                                                   # input of user will store here(number of ellements)
    arr = list(map(int, input().split()));                              # list of numbers that user type
    if(n >= 2 and n <= 10 and min(arr) >= -100 and max(arr) <= 100):    # check chellange ranges
        m = -100;                                                       # maximum number will store here(should intially have minimum number)
        for i in arr:                                                   # check every number of array
            if(i < max(arr)):                                           # check that number is not the maximum number
                m = max(m, int(i));                                     # compare between current number and prevouis max number
        print(m);                                                       # print second max number


'''
Sample Input 0:
5
2 3 6 6 5

Sample Output 0:
5

Explanation 0:
Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score.

'''
