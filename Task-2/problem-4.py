# Find the minimum distance between 2 similar numbers in a list.
# distance means -> the absolute difference between 2 indexes

l = input("Input:\n").split();  # store input in list
print("Output:");

minDis = len(l);                                            # initial value is maximum distance in list so len(l) = end - start + 1
for i in range(len(l)):                                     # loop to check each value in list
    if(l[i] in l[i + 1:]):                                  # create a list of the elements after current element and check whether is found in new list(if the element is duplicated in the origin list it would return true)
        minDis = min(minDis, l[i + 1:].index(l[i]) + 1);    # calculate the minimum distance
    #for n in range(i + 1, len(l)):         # loop to iterate on new list(elements after current element)
    #    if(l[i] ==  l[n]):                 # check whether the element is duplicated in list or not
    #        minDis = min(minDis, n - i);   # calculate the minimum distance
print(minDis);                                              # print the minimum distance

'''EX:
Input:
2 5 3 4 5 2
Output:
3

Explanation:
There are 2 options:
1-Distance between (2,2) which is 5 - 0 = 5
2-Distance between (5,5) which is 4 - 1 = 3
we want the minimum so we print 3
'''
