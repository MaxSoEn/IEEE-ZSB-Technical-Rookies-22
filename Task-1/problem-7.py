#That program asks the user for a number n and prints the sum of the 
#numbers 1 to n inclusive (only multiples of three or five are 
#considered in the sum)
def fun1(list1):
    sum1 = int(list1.pop());
    if(not(sum1 % 5 == 0 or sum1 % 3 == 0)):
        sum1 = 0;
    if(len(list1) == 0):
        return sum1;
    else:
        return sum1 + fun1(list1);

n = int(input("Inpput:\n"));
print("Output:");
print(fun1(list(range(1, n + 1))));

'''EX:
Input: 
15 
Output: 
60 
Explanation: 
Only numbers (3, 5, 6, 9, 10, 12, 15) as (3, 6, 9, 12) are multiples of 3 and (5, 10, 
15) are multiples of 5. So the answer will be 3 + 5 + 6 + 9 + 10 + 12 + 15 = 60
'''
