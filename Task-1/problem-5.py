#That program calculates compute the sum of the
#numbers in a list using three ways(3 functions)
def fun1(list1, n):
    sum1 = 0; 
    for i in range(n):
        sum1 += int(list1[i]);
    return sum1;
def fun2(list2, n):
    sum2 = 0;
    while(n > 0):
        n -= 1;
        sum2 += int(list2[n]);
    return sum2;
def fun3(list3, n):
    sum3 = int(list3[n - 1]);  #int(list3.pop());
    if(n <= 1):
        return sum3;
    else:
        return sum3 + fun3(list3, n - 1);
print("Input:");
n = int(input());
arr = input().split();
print("Output:");
print(fun1(arr, n));
print(fun2(arr, n));
print(fun3(arr, n));

'''Ex:
Input: 
3 
5 8 4 
Output: 
17 
17 
17
'''
