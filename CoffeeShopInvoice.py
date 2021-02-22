#Author: Ken Yu-ru Yang
#Description: Program to generating an informative invoice for the AM Coffee Shop

#!/usr/bin/env python3

#Welcome message and AM header
asteriskline = "*"*55
print(asteriskline)
print("Welcome to AM Coffee Shop")
print(asteriskline)
print("     /\        |\    /|")
print("    /  \       | \  / |")
print("   /    \      |  \/  |")
print("  /------\     |      |")
print(" /        \    |      |")
print("/          \   |      |")
print(asteriskline)

#Prompt user to enter date and pound
asteriskline = "*"*55
dashline = "-"*55
print()
date = int(input("Please enter date of the month (1-31): "))
pound = int(input("Please enter the amount of coffee in pounds: "))
print()
print(asteriskline)
print(dashline)
shipping_cost = float(0.86) * pound + float(1.50)
print("Shipping Cost: ", str(shipping_cost))
print(dashline)

#Define variables
cost = float(10.50) * int(pound)
tax1 = (31 - int(date)) / 3 / 100 * float(cost)
date += 1
tax2 = (31 - int(date)) / 3 / 100 * float(cost)
date += 1
tax3 = (31 - int(date)) / 3 / 100 * float(cost)
total1 = cost + tax1 + shipping_cost
total2 = cost + tax2 + shipping_cost
total3 = cost + tax3 + shipping_cost
date1 = int(date) - 2
date2 = int(date) - 1
date3 = int(date)

#Round
tax1 = round(tax1,2)
tax2 = round(tax2,2)
tax3 = round(tax3,2)
total1 = round(total1,2)
total2 = round(total2,2)
total3 = round(total3,2)

#Print receipt
print("Day","Cost","Tax","Total ",sep='    |    ',end='(Cost + Shipping + Tax)\n')
print(dashline)
print(date1,cost,tax1,total1,sep='    |    ')
print(dashline)
print(date2,cost,tax2,total2,sep='    |    ')
print(dashline)
print(date3,cost,tax3,total3,sep='    |    ')
print(dashline)
print()
print("Bye")



