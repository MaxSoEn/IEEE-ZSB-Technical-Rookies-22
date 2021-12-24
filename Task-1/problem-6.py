#That program asks the user for a number n and prints the sum of the 
#numbers 1 to n inclusive
def fun1(list1):
    sum1 = int(list1.pop());
    if(len(list1) == 0):
        return sum1;
    else:
        return sum1 + fun1(list1);

n = int(input("Inpput:\n"));
print("Output:");
print(fun1(list(range(1, n + 1))));

'''EX:
Input: 
5 
Output: 
15
'''
