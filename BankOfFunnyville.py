#Author: Ken Yu-ru Yang
#Description: Program that keeps track of user’s balance 

#!/usr/bin/env python3

#welcome message
print("Welcome to the Bank of Funnyville")
print()
starting_balance = int(input("Please enter the starting balance: "))

new_balance = 0

#validate for positive number
while (starting_balance <= 0): #invalid
    print("Invalid number. Please enter a positive number.")
    starting_balance = int(input("Please enter the starting balance: "))
print("-"*40)

#number is valid
more = 'y'
amount_entered = 0

while more == 'y':
    new_balance += int(starting_balance)
    transaction_type = input("Enter the type of transaction (w/d): ").lower()
    amount_entered = int(input("Enter the amount: "))

    #validate for positive number
    if (amount_entered < 0): #invalid
        print("Invalid number. Please enter a positive number.")
        continue    
    elif (amount_entered > 0 and transaction_type == "w"):
        new_balance = int(starting_balance) - int(amount_entered)
    elif (amount_entered > 0 and transaction_type == "d"):
        new_balance = int(starting_balance) + int(amount_entered)

    #print new balance
    print("New balance" + " = $" + str(new_balance))
    print("-"*40)

    #prompt continue or discontinue
    print("-"*40)
    more = input("Continue (y/n)? ").lower()

#print final balance
print("Your final balance: " + new_balance)
print("Bye!")
