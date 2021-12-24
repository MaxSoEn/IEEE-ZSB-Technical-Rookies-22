#Guessing Game
#guess a random number between 1 and 10
import random

r = random.randint(1,10);
n = int(input());
i = 1;
while(r != n):
    print("Wrong guess");
    n = int(input());
    i += 1;
else:
    print("Yay you got it", i, "tries", sep = ' ');
    
'''EX:
4
Wrong guess
5
Wrong guess
7
Wrong guess
3
Wrong guess
2
Yay you got it 5 tries
'''
