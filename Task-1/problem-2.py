#print prime numbers from 1 to n

def isPrime(u): # Check the number is prime or not
    if(u<2):
        return False;
    else:
        for x in range(2, int(u/2) + 1):
            if(i % x == 0):
                return False;
        else:
            return True;
    
n = int(input("Input:\n")); 
print("Output:");
for i in range(2, n + 1): # print prime numbers from 2 to n 
    if(isPrime(i)):
        print(i, end = ' '); # don't start new line

'''EX:
Input: 
15 
Output: 
2 3 5 7 11 13
'''
