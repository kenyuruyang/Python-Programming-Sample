#Author: Ken Yu-ru Yang
#Description: Program that asks the user for a set of integer numbers and does some processing on them

#!/usr/bin/env python3

#function: welcome message
def print_welcome():
    print("Welcome to the List Processing Program")
    print()

#function: prompt user for integer numbers and does some processing
def list_processing():
    number_list = []
    #prompt user for a set of integer
    while True:
        number = int(input("Please enter next number (Enter 0 to end): "))
        #input is valid
        if number > int(0) or number < int(0):
            number_list.append(number)
        #quit
        elif number == int(0):
            break
        #input is invalid
        else:
            print("Invalid input. Try again.")
            continue
    #calculate total and average of the list
    count = len(number_list)
    total = 0
    for number in number_list:
        total += number
    print("Count of numbers: ", str(count))
    average = total / len(number_list)
    print("Total: ", total, " , ", "Average: ", average)

    #prompt user for an old number and a new number for replacement
    while True:
        old_number = int(input("Enter the old number to be replaced: "))
        #input is valid
        if old_number in number_list:
            new_number = int(input("Enter the new number: "))
            break
        #input is invalid
        else:
            print("Invalid input. Try again.")
            continue    
    print("Before replacement: ")
    print(number_list)
    location = number_list.index(old_number)

    #replace old number with new number
    number_list.pop(location)
    number_list.insert(location, new_number)        
    print("After replacement: ")
    print(number_list)
    print("After sorting: ")

    #sort the list
    number_list.sort()
    print(number_list)
    print()

    #maximum number in the list
    maximum = max(number_list)
    print("Maximum number in the list: ", str(maximum))
    print()
    print("Good bye!")

#main function
def main():
    #call print_welcome function
    print_welcome()
    #call list_processing function
    list_processing()
    
#if this module is the main module
if __name__ == "__main__":
    #call the main() function
    main()

    
    
    

