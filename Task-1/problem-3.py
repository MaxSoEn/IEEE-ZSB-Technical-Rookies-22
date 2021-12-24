#Implement binary search

def binary_search(arr, n):
    low = 0;
    high = len(arr) - 1;
    mid = 0;
    while low <= high:
        mid = (high + low) // 2;
        #If n is greater, ignore left half
        if arr[mid] < n:
            low = mid + 1;
        #If n is smaller, ignore right half
        elif arr[mid] > n:
            high = mid - 1;
        #That means n is at mid
        else:
            return mid;
    #If element not found
    return -1;
 
#User Input
arr = input("Array\n").split();     #1 2 5 17 20 32
e = input("Element:\n");            # 20
 
#Call Function
i = binary_search(arr, e);
 
if i > -1:
    print("Element is found at index", str(i));
else:
    print("Element is not found in array");
