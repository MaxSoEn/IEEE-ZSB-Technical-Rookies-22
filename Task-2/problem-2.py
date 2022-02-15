# This program takes a sorted list as an input and removes the duplicates.

l = input("Input:\n").split();  # store input in list
print("Output:");
nl = [];                        # new list for store values that not duplicated
for i in l :                    # loop to pass on every value of list
    if(i not in nl):            # check if it found or not
        nl.append(i);           # add it to list
        print(i,end = ' ');     # print the value

# this part to print new list but this will slow the program
#for i in nl :
#    print(i,end = ' ');


'''EX:
Input:
1 1 2 3 4 4 5 6 7 7 8 9
Output:
1 2 3 4 5 6 7 8 9
'''
