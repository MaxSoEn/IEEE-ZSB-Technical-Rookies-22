# Find the minimum distance between 2 similar numbers in a list.
# distance means -> the absolute difference between 2 indexes

if __name__ == '__main__':

    num = list(map(int, input("Input:\n").split()));
    min_dist = len(num);

    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            if num[i] == num[j]:
                min_dist = min(j - i, min_dist);
                break;

    print("Output:", min_dist, sep = '\n')

'''EX:
Input:
2 5 3 4 5 2
Output:
3
Explanation:
There are 2 options:
1-Distance between (2,2) which is 5 - 0 = 5
2-Distance between (5,5) which is 4 - 1 = 3
we want the minimum so we print 3
'''
