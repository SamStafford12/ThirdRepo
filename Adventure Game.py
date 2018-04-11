import random
import time
class Person:
    def
class BountyHunter(Person):

    def __init_(self,name):
        self.name = name

def displayIntro():
    print("You have finally killed the rare Noah Mousseau, it took you a year")
    print("you are on your way home and come to crossroads you dont know which to take, one path leads home")
    print("You need to get home to be rewarded for the head of Noah Mousseau")
    print("and the other leads to a wild killer Thomas Bastis")
    print()

def choosePath():
    path = ""
    while path != "1" and path != "2": # input validation
        path = input("Which path will you choose? (1 or 2): ")

    return path

def checkPath(chosenPath):
    print("You head down the path")
    time.sleep(2)
    print("there's a random shack nearby that looks familiar, that must be a good sign...")
    time.sleep(2)
    print("But your skin begins breakout with monsterous chicken pocks...")
    print()
    time.sleep(2)

    correctPath = random.randint(1, 2)

    if chosenPath == str(correctPath):
        print("The chicken pocks was just a attack from your home village they didnt recognize you!")
        print("Welcome home bitch!")
    else:
        print("A wild Thomas Bastis Jumps out of a bush")
        print("You get absolutely fucked")
        print("there is no record left of your existence except for the head of Noah Mousseau.")


playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    choice = choosePath()
    checkPath(choice) # choice is equal to "1" or "2"
    playAgain = input("Do you want to play again? (yes or y to continue playing): ")
    
