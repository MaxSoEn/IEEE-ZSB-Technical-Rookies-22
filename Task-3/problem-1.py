# You have n (n > 1) bottles of water, each bottle is described by remaining 
# volume of water and capacity. You should determine if you can pour all 
# remaining water into just 2 bottles. 
# Input: 
# The first line is n(number of bottles) 
# The next n lines contain 2 space-separated integers (remaining volume and capacity) 
# Output: 
# print "Yes" if you can pour all the water into 2 bottles, otherwise print "No". 

if __name__ == '__main__':                                      # to prevent program (check if it run or use in another program as a module
    bottles = [];                                               # 
    maxCapacity = [0, 0];                                       # 
    index = -1;                                                 # 
    for n in range(int(input("Input:\n"))):                     # loop for each bottle info
        info = list(map(int, input().split()));                 # store info in nested list
        if(maxCapacity[0]<  info[1]):                           #
            maxCapacity[0] =  info[1];                          #
            index = len(bottles);                               #
        bottles.append(info);                                   # add info of each bottle to main list
    s = 0;                                                      #
    for i in range(len(bottles)):                               #
        s += bottles[i][0];                                     #
        if(i != index):                                         # 
            maxCapacity[1] = max(maxCapacity[1], bottles[i][1]);# 
    print("Output:");                                           #
    if(s > maxCapacity[0] + maxCapacity[1]):                    #
        print("No");                                            #
    else:                                                       #
        print("Yes");                                           #


'''EX: 
Input: 
2 
3 6 
5 6 
Output: 
Yes 


''EX2: 
Input: 
3 
6 6 
8 10 
9 12 
Output: 
No 

'''
