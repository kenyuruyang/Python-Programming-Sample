#Author: Ken Yu-ru Yang

# Program to simulate a speed dialer
# Complete the four functions listed below that work with
# two global lists that manage a dialer with 5 fixed slots.
# Initialize the dialer with empty data.

#!/usr/bin/env python3

dialerNames = ["Empty", "Empty", "Empty", "Empty", "Empty"]
dialerNumbers = ["Empty", "Empty", "Empty","Empty", "Empty"]

#function to show the current dialer data
def printList():
    #Implement this function
    #slots = [["Empty", "Empty"],
             #["Empty", "Empty"],
             #["Empty", "Empty"],
             #["Empty", "Empty"],
             #["Empty", "Empty"]]
    item_names = ["Empty", "Empty", "Empty", "Empty"]
    item_numbers = ["Empty", "Empty", "Empty", "Empty"]
    printContactList(item_names, item_numbers)
    index = 1
    for index in range(len(item_names)):
        print(index+1, item_names[index], item_numbers[index], sep="\t")
        index += 1

    
#Function to handle dial by slot number command which
#   prompts the user for the slot number
#   validates the slot number
#   if not within valid range (1 through 5), prints "Invalid slot number"
#   else checks if the slot at given slot number is empty, if so prints "Slot empty"
#   else prints "Calling name ........xxx-xxx-xxxx"
# E.g. If user enters 3 and slot number 3 (values at index 2 in above lists) had
#   name = "Susan" and number 4255551212, this function will print
#   "Dialing Susan ........425-555-1212"
def dialBySlot():
    #Implement this function
    slot_number = input("Enter the slot number: ")
    print("Calling " + slot_number + "........" + row[slot_number-1][1]) 
        
#Function to handle dial by name command which
#   prompts the user for the name
#   checks if the name is present in dialerNames list (make the comparison
#   case-insensitive)
#   if not present prints "Name not found."
#   else prints "Calling name ....xxx-xxx-xxxx"
# E.g. If user enters "Susan" and slot number 3 (values at index 2
#   in above lists) had name = "Susan" and number 4255551212,
#   dialByName() will print
#   "Dialing Susan ........425-555-1212"
def dialByName():
    #Implement this function
    name = input("Enter the name: ")
    print("Calling " + name + "........" + row[name-1][1]) 
    
#Function to handle update by slot number command which
#   prompts the user for the slot number to be updated
#   validates the slot number, if not within valid range, prints "Invalid slot number"
#   else, prompts the user for the new name and new number
#   and updates entries for the slot number.
#   prints "Updated slot number X" where X is the slot number user entered.

def updateSlot():
    #Implement this function
    slots = []
    while True:
        index = int(input("Enter the slot number: "))
        if (index < 6):
            new_name = input("Enter new name: ")
            new_number = input("Enter new number: ")
            slots.pop(index-1)
            slots.insert(row[index-1][0], new_name)
            slots.insert(row[index-1][1], new_number)
        else:
            break
    print("Updated slot number " + index)

def main():
    print('''Welcome to the Speed Dialer.
Commands:
p for print \tn dial by name
u for update\ts dial by slot
e for exit''')
    
    item_names = ["Empty", "Empty", "Empty", "Empty"]
    item_numbers = ["Empty", "Empty", "Empty", "Empty"]
    printContactList(item_names, item_numbers)
    
    command = input('''Please enter command(p/n/s/u/e): ''').lower()
    while (not command.startswith('e')):
        if (command.startswith('p')):
            printList()
        elif (command.startswith('n')):
            dialByName()
        elif (command.startswith('s')):
            dialBySlot()
        elif (command.startswith('u')):
            updateSlot()
        command = input("Please enter command(p/n/s/u/e): ").lower()
    print("Goodbye!")

if __name__ == "__main__":
    main()
