# this program implementate the Insertion Sort
# Move elements of arr[0..i-1], that are greater than key,
# to one position ahead of their current position


arr = input("Input:\n").split();    # store input in array
print ("Output:");                  
for i in range(1, len(arr)):        # start loop from second element in array
    key = arr[i];                   # store the value of element in variable
    j = i-1;                        # j index to the element before i
    while j >=0 and key < arr[j] :  # loop will check that the element of i is less than element of j
        arr[j+1] = arr[j];          #  place element of j to right
        j -= 1;                     # check the rest of elements on the left side
    arr[j+1] = key;                 # place the element of i at last index we reached
for i in range(len(arr)):           # print the array after sorting
    print (arr[i], end = ' ');

'''EX:
Input:
1 5 83 36 32 93 12 4 2
Output:
1 12 2 32 36 4 5 83 93

'''
