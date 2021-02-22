#Author: Ken Yu-ru Yang
#Description: Program to calculate average miles per gallon

#!/usr/bin/env python3

#welcome message
print("Welcome to the Average MPG Calculator")
print()

#prompt user to enter the starting odometer reading in miles 
starting_odometer_reading = float(input("Please enter the starting odometer reading in miles: "))
print()

#validate that the reading is positive
while starting_odometer_reading < 0:
    print("The starting odometer reading must be a positive number.")
    starting_odometer_reading = float(input("Please enter the starting odometer reading in miles: "))
print()
print("_________________________________________________________________________")
    
#initialize variables
current_odometer_reading = 0
leg_number = 0
total_fuel = 0
total_miles = 0
more_input = "y"

#prompt user to enter the odometer reading and amount of fuel in gallons used for the next leg of journey 
while more_input == "y":
    leg_number += 1
    current_odometer_reading = float(input("Please enter new odometer reading in miles for leg #" + str(leg_number) + ": "))
    fuel_consumed = float(input("Please enter fuel consumed in gallons for leg #" + str(leg_number) + ": "))
    total_fuel += fuel_consumed

    #validate that the odometer reading is more than the last odometer reading and that the fuel is a positive number
    if current_odometer_reading > 0 and current_odometer_reading > starting_odometer_reading:

        #compute the miles per gallon (mpg) for this leg
        total_miles += current_odometer_reading
        mpg = (current_odometer_reading - starting_odometer_reading) / fuel_consumed
        starting_odometer_reading = current_odometer_reading
        mpg = round(mpg,2)

        #print the mpg for this leg
        print("Average MPG for leg #" + str(leg_number) + " = " + str(mpg))

        #ask user if there are additional legs for which the program should continue
        more_input = input("Continue (y/n)?: ")

    #if the entered value of fuel consumed is negative number or if the entered value of new odometer reading is lower than the last one, repeat above loop
    else:
        print("Fuel consumed needs to be positive and new odometer reading needs to be higher than the last one. \n")
        continue
    print("_________________________________________________________________________")

#print the total number of legs in the entire journey
print("Total number of legs in the entire journey: " + str(leg_number))

#calculate and print the final average MPG for the entire journey
average_MPG = total_miles / total_fuel
average_MPG = round(average_MPG,2)
print("Final average MPG for the entire journey: " + str(average_MPG))
print("Bye!")
