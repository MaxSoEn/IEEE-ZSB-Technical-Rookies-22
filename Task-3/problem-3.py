# this program generates a password which consists of 10 characters
# (numbers, lowercase letters, uppercase letters and other characters). 
# It should contain at least 1 number and at least 1 of these characters [@, #, $, %, &]

import string # to generate all ascii chars
import random # to randomize choice from lists

# function generates random and strong password
def passwordGenerator( length = 8, min_sym = 0, min_num = 0, min_lower = 0, min_upper = 0):
    sympols = ['@', '#', '$', '%', '&'];                        # ascii code 64, 35 - 38
    numbers = list(string.digits);                              # ascii code 48 - 57
    alpha_l = list(string.ascii_lowercase);                     # ascii code 97 - 122
    alpha_u = list(string.ascii_uppercase);                     # ascii code 65 - 90
    characters = list(alpha_u + alpha_l  + numbers  + sympols); # all ascii characters(can be used in password)

    if(length < min_sym + min_num + min_upper + min_lower):     # check if the length of password is bigger than minimum conditions or not
        print("Error...");                                      # print error
        exit(-1);                                               # exit program with code -1

    password = [];                                              # password chars will be store in this list

    random.shuffle(sympols);                                    # shuffle the list of sympols
    for i in range(min_sym):
        password.append(random.choice(sympols));                # generate minimum sympols in password

    random.shuffle(numbers);                                    # shuffle the list of numbers
    for i in range(min_num):
        password.append(random.choice(numbers));                # generate minimum numbers in password

    random.shuffle(alpha_l);                                    # shuffle the list of lowercase letters
    for i in range(min_lower):
        password.append(random.choice(alpha_l));                # generate minimum lowercase letters in password

    random.shuffle(alpha_u);                                    # shuffle the list of uppercase letters
    for i in range(min_upper):
        password.append(random.choice(alpha_u));                # generate minimum  in uppercase letters password

    random.shuffle(characters);                                 # shuffle the list of rest of characters
    for i in range(len(password), length):
        password.append(random.choice(characters));             # add random chars to complete the length of password

    random.shuffle(password);                                   # shuffle the list of password chars(generate a complex password)
    return "".join(password);                                   # convert list to string

if __name__ == '__main__':
    length = 10;
    sym = 1;
    num = 1;
    a_lower = 0;
    a_upper = 0;
    Pass = passwordGenerator(length, sym, num, a_lower, a_upper);   # call function
    print(Pass);                                                    # print password
