#Author: Ken Yu-ru Yang
#Description: Program that stimulates the "Rock-Paper-Scissors" game

#!/usr/bin/env python3

#import random function
from random import randint

#function: welcome message and rule of game
def printWelcome():
    print("Welcome to Rock/Paper/Scissors Game")
    print()
    print("Rules of the game: \n"+
          "\tYou and the Computer will each pick (r)ock, (p)aper or (s)cissors.\n"+
          "\tThe winner will be decided using following policy:\n"+
          "\tRock wins over Scissors but loses to Paper.\n"+
          "\tScissors wins over paper but loses to Rock.\n"+
          "\tPaper wins over Rock but loses to Scissors.")
    print()
    print("\tLet the game begin!! Enter 'q' to quit.")
    print()

#function: prompt user to pick a choice
def getUserPick():
    while True:
        user = str(input("Your turn. Pick (r)ock, (p)aper, (s)cissors: "))
        #entry is invalid
        if user != "r" and user != "p" and user != "s" and user != "q":
            print("Invalid input. Please try again.")
            continue
        #entry is valid
        else:
            break
    return user
    
#function: compare choices between user and computer
def getResult(user, computer):
    if (user == "r" and computer == "Rock") or (user == "p" and computer == "Paper") or (user == "s" and computer == "Scissors"):
        return "tie"
    if user == "r" and computer == "Scissors":
        return "user"
    if user == "s" and computer == "Paper":
        return "computer"
    if user == "p" and computer == "Rock":
        return "user"

#function: stimulate computer to pick its choice
def pickRPS():
    choiceList = ["Rock", "Paper", "Scissors"]
    computer = choiceList[randint(0,2)]
    return computer

#main function
def main():
    #call printWelcome function
    printWelcome()
    #initialize all counts to zeros
    countUserWins = 0
    countComputerWins = 0
    countTies = 0
    countTotal = 0
    #call getUserPick function
    user = getUserPick()
    #loop for continue entries
    while user.lower() != "q":
        #call pickRPS function
        computer = pickRPS()
        #call getResult function
        print("You picked" + " " + str(user.lower()) + " and Computer picked " + str(computer))
        getResult(user, computer)
        #get input from the user
        winner = getResult
        #announce winner and increment counts
        if (user == "r" and computer == "Rock") or (user == "p" and computer == "Paper") or (user == "s" and computer == "Scissors"):
            print("It's a tie!")
            countTies += 1
        elif user == "r" and computer == "Scissors":
            print("You win")
            countUserWins += 1
        elif user == "s" and computer == "Paper":
            print("You win")
            countUserWins += 1
        elif user == "p" and computer == "Rock":
            print("You win")
            countUserWins += 1
        else:
            print("Computer wins")
            countComputerWins += 1
        countTotal += 1
        #call getUserPick function again
        user = getUserPick()
    print()
    #print final counts
    print("Number of rounds: " + str(countTotal))
    print("Number of times you won: " + str(countUserWins))
    print("Number of times Computer won: " + str(countComputerWins))
    print("Number of ties: " + str(countTies))
    print("Bye!")

#if this module is the main module
if __name__ == "__main__":
    #call the main() function
    main()
