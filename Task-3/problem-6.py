# You are given a number that contains 4 digits with at least two distinct digits. 
# Your program should perform the following routine on the number: Arrange the digits in descending order and in ascending order
# (adding zeros to fit it to a 4-digit number), and subtract the smaller number from the bigger number.
# Then repeat the previous step. Performing this routine will always cause you to reach a fixed number: 6174.
# Your program should return the number of times this routine must be performed until 6174 is reached.

num = input("Input\n");
asc = ''.join(sorted(num));
des = ''.join(sorted(num, reverse = True));
diff = str(abs(int(des) - int(asc))).zfill(4);
count = 1;
while(int(diff) != 6174 and int(diff) > 0):
    asc = ''.join(sorted(diff));
    des = ''.join(sorted(diff, reverse = True));
    diff = str(abs(int(des) - int(asc))).zfill(4);
    count += 1;
print("Output:");
print(count);


'''EX1:
Input: 
2111 
Output: 
5 

''EX2: 
Input: 
9831 
Output: 
7


For example, if num is 3524 your program should return 3 because of the following steps:

(1) 5432 - 2345 = 3087 
(2) 8730 - 0378 = 8352 
(3) 8532 - 2358 = 6174
'''
