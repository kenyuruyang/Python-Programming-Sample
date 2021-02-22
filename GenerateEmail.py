#Author: Ken Yu-ru Yang
#Description: ## Program to generate emailId and temporary password given a students's fullname
## for funnyville highschool following given guidelines.

#!/usr/bin/env python3

import random

# Useful global constants
LETTERS = 'abcdefghijklmnopqrstuvwxyz'
SPECIAL_CHARACTERS = '!@#$%'

def generateEmailID(fullname):
    ''' Generate and return email id.
    takes the user’s full name in the form “First Last” OR “First Middle Last”.
    Generates and returns email id which 
        is all lower case.
        is of the form “last.first@fhs.edu” if no middle name provided or
        or of the form “last.first.middIeInitial@fhs.edu” if middle name is provided. '''
    names = fullname.split()
    firstname = names[0]
    middlename = names[1]
    lastname = names[2]
    email = (names[2] + "." + names[0] + "." + middlename[0] + "@" + "fhs.edu")
    return email

def generatePassword(fullname):
    '''Generates and returns temporary password such that:
    The temporary password

        starts with the first letter of the first name, made upper case.
        followed by two random lower case letters (can be repeated)
        followed by a two digit random number (can have repeated digits, but has to be 2 digits long)
        followed by a single random letter from '!@#$%'
        followed by the last letter of the last name, made upper case. See sample runs below.   
    '''
    names = fullname.split()
    firstname = names[0]
    middlename = names[1]
    lastname = names[2]
    password = (firstname[0].upper() + random.choice(LETTERS) + random.choice(LETTERS) +
          str(random.randint(1, 9)) + str(random.randint(1, 9)) + random.choice(SPECIAL_CHARACTERS) +
          lastname[-1].upper())
    return password
    

def main():
    print("Welcome to Funnyville High School registration")
    ans = 'y'
    while (ans == 'y'):
        fullname = input("\nEnter your full name: ").strip()
        email = generateEmailID(fullname)
        password = generatePassword(fullname)
        # Give user email id and password
        print("Your FHS email id:", email)
        print("Your temporary passwd:", password)

        #prompt to check if want to continue
        ans = input("\nContinue?(y/n)").lower()
        
    print("Good Bye!")

    
if __name__ == "__main__":
    main()
    
