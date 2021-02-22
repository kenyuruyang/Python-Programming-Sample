#Author: Ken Yu-ru Yang
#Description: ## Program that keeps track of the inventory of items a wizard is carrying. 

#!/usr/bin/env python3

#function: display title
def display_title():
    print("The Wizard Inventory program")
    print()    

#function: display menu
def display_menu():
    print("COMMAND MENU")
    print("show - Show all items")
    print("grab - Grab an item")
    print("edit - Edit an item")
    print("drop - Drop an item")
    print("exit - Exit program")
    print()

#function: display list of items in inventory
def show(inventory):
    item_number = 1
    for item in inventory:
        print(str(item_number) + ". " + item)
        item_number += 1
    print()

#function: to grab (to add) an item into inventory
def grab_item(inventory):
    #valid input: items less then 4 in inventory
    if len(inventory) < 4:
        item = input("Name: ")
        inventory.append(item)
        print(item + " was added.\n")
    #invalid input: inventory too full
    else:
        print("You can't carry any more items. Drop something first.")
    print()

#function: to edit an item in inventory
def edit_item(inventory):
    item_number = int(input("Number: "))
    #invalid input: out of range
    if item_number < 1 or item_number > len(inventory):
        print("Invalid item number.\n")
    #valid input: in range
    else:
        updated_name = input("Updated name: ")
        inventory.pop(item_number-1)
        inventory.insert(item_number-1, updated_name)
        print("Item number " + str(item_number) + " was updated.")
    print()

#function: to drop (to delete) an item in inventory
def drop_item(inventory):
    item_number = int(input("Number: "))
    #invalid input: out of range
    if item_number < 1 or item_number > len(inventory):
        print("Invalid item number.\n")
    #valid input: in range
    else:
        item = inventory.pop(item_number-1)
        print(item + " was dropped.\n")
    print()

#main function
def main():
    #call display_title function
    display_title()
    #call display_menu function
    display_menu()

    #start with these 3 items
    inventory = ["wooden staff", "wizard hat",
                 "cloth shoes"]
    #while loop to call functions 
    while True:        
        command = input("Command: ")        
        if command == "show":
            show(inventory)
        elif command == "grab":
            grab_item(inventory)
        elif command == "edit":
            edit_item(inventory)
        elif command == "drop":
            drop_item(inventory)
        elif command == "exit":
            break
        #invalid input
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

#if this module is the main module
if __name__ == "__main__":
    #call the main() function
    main()
