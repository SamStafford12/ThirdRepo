import random
import time

def die():
    return random.randint(1,6)
    
class Person:

    def __init__(self,life,damage,maxdamage,maxlife):
        self.life=life
        self.damage=damage
        self.maxdamage-maxdamage
        self.maxlife=maxlife

class Bountyhunter(Person):

    def __init__(self):
        super().__init__(life=100,damage=50,maxdamage=50,maxlife=10)

class Thomas(Person):

    def __init__(self):
        super().__init__(life=815,damage=4000,maxdamage=4000,maxlife=815)

class Noah(Person):

    def __init__(self):
        super().__init__(life=69,damage=11,maxdamage=11,maxlife=69)
        
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
    print("You might be close.")
    print()
    time.sleep(2)

    correctPath = random.randint(1, 2)

    if chosenPath == str(correctPath):
        print("You come over a hilltop and you see your hometown!")
        time.sleep(2)
        print("Welcome home")
        time.sleep(2)
        print("You now are a famous hero for killing Noah and bringing his head back")
        
    else:
        print("Not good you see Thomas Bastis in a bush")
        time.sleep(2)
        print("you think to yourself how you want to go about this")
        time.sleep(2)
        print("Thomas spots you contemplating and springs towards you")
        x = die()
        if x > 1:
            print("You got raped by Thomas Bastis")
        else:
            print("You magically killed thomas you are now a famous hero.")



playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    choice = choosePath()
    checkPath(choice) # choice is equal to "1" or "2"
    playAgain = input("Do you want to play again? (yes or y to continue playing): ")
    
