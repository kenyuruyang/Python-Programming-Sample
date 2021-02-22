#Author: Ken Yu-ru Yang
#Description: Program that calculates total cost of meal at different tipping percentages

#!/usr/bin/env python3

def costWithTip(meal_cost, tip_percentage):
    #calculate tip and total cost
    tip = meal_cost * tip_percentage / 100
    total_cost = meal_cost + tip
    return total_cost

def main():
    #display a welcome message
    print("Welcome to Tip Calculator")
    print()
    while True:
        #get input
        meal_cost = int(input("Cost of meal: "))
        print("-"*40)
        #validate input
        if meal_cost <= 0:
            print("Please enter a positive amount. \n")
            continue
        else:
            break
        print("-"*40)
    #call costWithTip method 3 times
    tip_percentage = 0
    for tip_percentage in range(15, 30, 5):
        #get and display cost with tip
        total_cost = costWithTip(meal_cost, tip_percentage)
        print("Tip: " + str(tip_percentage) + "%")
        print("Total amount including tip: " + "$" + str(round(total_cost,2)))
        print("-"*40)
        
    print("Goodbye!")

if __name__ == "__main__":
    main()
    
