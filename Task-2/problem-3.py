# This program randomly generates a 3-digit number and ask the user to guess a 3-digit number.
# For every digit that the user guessed correctly in the correct place, they have a "hit".
# For every digit the user guessed correctly in the wrong place is a "miss".
# Every time the user makes a guess, program tells them how many hits and misses they have.
# Once the user guesses the correct number, the game is over.
# print the number of attempts they needed to guess the number.
import random

r = str(random.randint(0,999)).zfill(3);                # create a random 3-digit number (ex:427)
hit = 0;                                                # calculate how many numbers are correct and in correct place
miss = 0;                                               # calculate how many numbers are correct but in wrong place
attempt = 0;                                            # calculate how many times user guess wrong 
n = ''                                                  # store user number in variable
while(n != r):                                          # if user guess the number, the game is over
    n = input("Enter a 3-digit number:\n>>> ").zfill(3);# store user number in variable
    if(n != r):                                         # user guess wrong
        attempt += 1;                                   # increase variable by 1
                                                        # hit and miss check where number matches
        hit = int(n[0] == r[0]) + int(n[1] == r[1]) + int(n[2] == r[2]); 
        miss = int(n[0] == r[1] or n[0] == r[2]) + int(n[1] == r[0] or n[1] == r[2]) + int(n[2] == r[0] or n[2] == r[1]);
        print(hit, "hit", miss, "miss", sep = ' ');     # print value of hit and miss
print("number of guess :", attempt);                    # if the game is over program will print number of wrong guess

'''EX:
if the random number is 427
The program will look like this:
Enter a 3-digit number:
>>> 412
1 hit 1 miss
>>> 413
1 hit 0 misses
'''
