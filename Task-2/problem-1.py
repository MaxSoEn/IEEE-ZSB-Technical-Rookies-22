# This program asks the user for a string and tests whether it's a
# palindrome. If it's a palindrome print "yes", if not, print "no".

s = input("Input:\n");  # ask user for input
print("Output:");
if(s == s[::-1]):       # check whether string is the same if you reversed it
    print("yes");       # print yes
else:
    print("no");        # print no

'''EX1:
Input:
start
Output:
no

''EX2:
Input:
level
Output:
yes
'''
