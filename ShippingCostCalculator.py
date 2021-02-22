#Author: Ken Yu-ru Yang
#Description: Program to calculate shipping cost

#!/usr/bin/env python3

#welcome message
print("Welcome to Shipping Calculator")
print("-"*50)
print("Today's cost of 1 pack of Printer Paper is $5.5")
print("-"*50)

#prompt user to enter number of order
number_ordered = int(input("How many packs do you want to order?" ))
print("-"*50)

#calculate cost of order
cost_ordered = number_ordered * 5.5

#calculate shipping cost
if (number_ordered < 55):
    shipping_cost = 5.95
elif (number_ordered >= 55 and number_ordered <= 99.99):
    shipping_cost = 7.95
elif (number_ordered >= 100 and number_ordered <= 149.99):
    shipping_cost = 9.95
else:
    shipping_cost = 0

#calculate total cost
total_cost = float(cost_ordered) + float(shipping_cost)

#print cost of items, shipping cost, and total cost
print("Cost of items ordered: " + str(cost_ordered))
print("Shipping cost: " + str(shipping_cost))
print("Total Cost: " + str(total_cost))
print("-"*50)
print("Bye")
