#Author: Ken Yu-ru Yang
#Description: Program to compute and report the day of the week using Zeller's algorithm

#!/usr/bin/env python3

#prompting user for information
month = int(input("Enter month: "))
date = int(input("Enter the date: "))
year = int(input("Enter the year: "))

#step 1: adjusting month and year
if(month == 1):
    a = 11
    adjusted_year = year - 1
elif(month == 2):
    a = 12
    adjusted_year = year - 1
elif(month == 3):
    a = 1
    adjusted_year = year
elif(month == 4):
    a = 2
    adjusted_year = year
elif(month == 5):
    a = 3
    adjusted_year = year
elif(month == 6):
    a = 4
    adjusted_year = year
elif(month == 7):
    a = 5
    adjusted_year = year
elif(month == 8):
    a = 6
    adjusted_year = year
elif(month == 9):
    a = 7
    adjusted_year = year
elif(month == 10):
    a = 8
    adjusted_year = year
elif(month == 11):
    a = 9
    adjusted_year = year
elif(month == 12):
    a = 10
    adjusted_year = year

#step 2: calculating intermediate values
c = int(adjusted_year)%100
b = date
d = (int(adjusted_year)-int(c))//100

print("a b c d = ", a, b, c, d)

#step 3: computing final values
w = (13*int(a)-1)//5
x = int(c)//4
y = int(d)//4
z = int(w) + int(x) + int(y) + int(b) + int(c) - 2*int(d)
r = int(z)%7

print("w x y z r = ", w, x, y, z, r)

#step 4: adjusting r and printing out day of the week
if(r == 0):
    print("Day of the week: Sunday")
elif(r == 1):
    print("Day of the week: Monday")
elif(r == 2):
    print("Day of the week: Tuesday")
elif(r == 3):
    print("Day of the week: Wednesday")
elif(r == 4):
    print("Day of the week: Thursday")
elif(r == 5):
    print("Day of the week: Friday")
elif(r == 6):
    print("Day of the week: Saturday")
