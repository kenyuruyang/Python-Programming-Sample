#Author: Ken Yu-ru Yang
#Description: Program to detecting the type of a triangle

#!/usr/bin/env python3

#Welcome message
print("Welcome to Triangle Dectector")

#Prompt the user to enter the length of the sides of triangle
side1 = input("Enter the length of a side of a triangle (a positive integer): ")
side2 = input("Enter the length of a side of a triangle (a positive integer): ")
side3 = input("Enter the length of a side of a triangle (a positive integer): ")

#Change the type of side from string to integer
side1 = int(side1)
side2 = int(side2)
side3 = int(side3)

#Calculate the triangle
if (side1 + side2 <= side3) or (side2 + side3 <= side1) or (side1 + side3 <= side2):
    print("It is not a valid triangle")
elif (side1 == side2 == side3):
    print("It is an equilateral triangle")
elif (side1 == side2) and (side1 + side2 > side3) or (side2 == side3) and (side2 + side3 > side1) or (side3 == side1) and (side3 + side1 > side2):
    print("It is an isosceles triangle")
else:
    print("It is a scalene triangle")

print("Good bye!")
