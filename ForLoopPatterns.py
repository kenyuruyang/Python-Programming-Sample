#Author: Ken Yu-ru Yang
#Description: Program that creates a christmas tree and a mirror pattern using for-loops given an odd number

#!/usr/bin/env python3


#welcome message
print("Welcome to Pattern Generator")
print()

#prompt user to enter an odd number between 7 and 15 (both inclusive)
while True:
    odd_number = input("Please enter the size of the patterns (an odd number between 7 and 15): ")
    #valid
    if odd_number == "7" or odd_number == "9" or odd_number == "11" or odd_number == "13" or odd_number == "15":
        break
    #invalid
    else:
        print("Size should be an odd number between 7 and 15")
        continue

#christmas tree pattern and mirror pattern
print()
print("Christmas Tree Pattern of Size" + " " + str(odd_number))

#tree leaves
for line_and_number_of_stars in range(1, int(odd_number)+2, 2):
    number_of_spaces = (int(odd_number) - int(line_and_number_of_stars)) / 2
    number_of_spaces = int(number_of_spaces)
    print(" "*number_of_spaces + "*"*line_and_number_of_stars)

#tree trunk (out of the for loop)
trunk_number_of_spaces = int(odd_number) // 2
trunk_number_of_spaces = int(trunk_number_of_spaces)
print(" "*trunk_number_of_spaces + "*")
print(" "*trunk_number_of_spaces + "*")

#tree base (out of the for loop)
base_number_of_spaces = (int(odd_number) - 3) / 2
base_number_of_spaces = int(base_number_of_spaces)
print(" "*base_number_of_spaces + "*"*3)
print()

print("Mirror Image Pattern of Size" + " " + str(odd_number))
#mirror top
for line_and_number_of_As_left_a in range(1, int(odd_number)+1, 1):
    number_of_spaces_b = int(odd_number)*2 - line_and_number_of_As_left_a*2
    number_of_As = line_and_number_of_As_left_a*2
    print("A"*line_and_number_of_As_left_a + " "*number_of_spaces_b + "A"*line_and_number_of_As_left_a)

#mirror bottom
for number_of_As_left_b in range(int(odd_number)-1, 0, -1):
    number_of_spaces_c = (int(odd_number) - number_of_As_left_b) * 2
    print("A"*number_of_As_left_b + " "*number_of_spaces_c + "A"*number_of_As_left_b)
print()

print("Bye")
