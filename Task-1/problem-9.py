#That program takes input a number, n > 0 and generates the first n 
#Fibonacci F(n) = F(n-1) + F(n-2)
#0 1 1 2 3 5 8 13 21 .....
n = int(input("Input:\n"));
t = 1;  # calculate the new term of Fibonacci
f = [0]; # Fibonacci terms in array
for i in range(1, n): # 100 for 100 terms
    f.append(t); # add the new term to array
    t = f[i] + f[i-1]; # calculate the new term of Fibonacci
print("Output:");
for i in f:
    print(i, end = ' ');

'''EX:
Input: 
8 
Output: 
0 1 1 2 3 5 8 13 
'''
