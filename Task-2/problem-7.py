# https://www.hackerrank.com/challenges/find-a-string/problem
# find a string
# find the number of occurrences of a substring in a string.

def count_substring(string, sub_string):
    n = 0;                                                  # variable for count of sub strings
    if(len(string) >= 1 and len(string) <= 200):            # formate condition
        for i in range(len(string)):                        # loop for each char in string
            if(sub_string == string[i:i+len(sub_string)]):  # if sub string is equal to string from current char to the length of string
                n += 1;                                     # increase n by 1
    return n;                                               # return the count after it calculated

if __name__ == '__main__':
    string = input().strip();                   # user string after removing white spaces at the begin and end
    sub_string = input().strip();               # user sub string after removing white spaces at the begin and end
    
    count = count_substring(string, sub_string);# call function and store return in count
    print(count);                               #print the value of count

'''
Sample Input:
ABCDCDC
CDC

Sample Output:
2

'''
