# You have a sequence of letters that is repeated infinitely
# Print the number of r's in the first n letters.
# Input:
# The first line represents the sequence of letters
# The second line represents n.


l = input("Input:\n").lower();
n = int(input());
s = '';
c = 0;
while(len(s) < n):
    if(l[len(s)%len(l)] == 'r'):
        c += 1;
    s += l[len(s)%len(l)];
print("Output:", c, sep = '\n');


'''EX:
Input:
rar
10
Output:
7

Explanation:
'rar' is repeated infinitely, we only take the first n letters and check how many r's
are in there. The first n(10 in the example) letters will be 'rarrarrarr'
'r' is repeated 7 times so we print 7.
'''
