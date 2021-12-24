#That program takes a sentence and prints it,
#word per line,
#in a rectangular frame

arr = input("Input:\n").split();
m = max(arr, key = len);
print('*' * (len(m) + 2));
for s in arr:
    print('*', s, ' ' * (len(m) - len(s)), '*', sep = '');
print('*' * (len(m) + 2));    

'''EX:
Input:
Hello World in a frame
Output:
*******
*Hello*
*World*
*in   *
*a    *
*frame*
*******

'''
