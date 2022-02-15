# https://www.hackerrank.com/challenges/nested-list/problem
# Nested Lists
# In a classroom of N students, find the student with the second lowest grade.

if __name__ == '__main__':              # to prevent program (check if it ru or use in another program as a module
    n = [];                             # array with the name of students
    s = [];                             # array with the score of students
    for _ in range(int(input())):       # loop for each name and grade of student
        name = input();                 # store the name
        score = float(input());         # store the score
        n.append(name);                 # add name to array
        s.append(score);                # add score to array
    m = max(s);                         # second minimum number will store here(should intially have maximum number)
    for i in s:                         # check every number of score(student grade)
        if(i > min(s)):                 # check that number is not the minimum number
            m = min(m, float(i));       # compare between current number and prevouis min number and store it
    o = [];                             # array of the output names
    for i in range(len(n)):             # loop to add name of students with second lowest score to array
        if(s[i] == m):                  # if the student number i has a score then it will be added to array
            o.append(n[i]);             # add the name to the array
    o = sorted(o);                      # sort array alphapitically
    for i in o:                         # loop to print names of students
        print(i);


'''
Sample Input 0
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output 0
Berry
Harry

Explanation 0
There are  students in this class whose names and grades are assembled to build the following list:
python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.
'''
