"""A Random Game"""
__author__ = "730386298"

def playagain(): #above and beyond
    answer = input("Do you want to play again? ")
    if answer == "yes":
        print("Okay")
        main()
    else:
        print("Okay. Goodbye.")

def greet() -> None:
    print(f"Welcome to the game, {player} !!")

def main() -> None:
    greet()
    levelone()

name = input("What is your player name? ")
player = name
points = 0
HAPPY_FACE = "\U00000000"


def levelone() -> None:
    print("There are three doors: red, yellow, and blue")
    choice = input("Do you choose red, yellow, or blue? ")
    if choice == "red":
        print("You lose! Goodbye.")
        print(points)
        playagain()
    else:
        if choice == "yellow":
            print(f"Congrats, {player}. You have moved on to level two, where your fate will be determined randomly. Good luck.")
            print("\U0001f600")
            levelone_pointsa = points + 10
            print(f"Points: {levelone_pointsa}")
            leveltwo(levelone_pointsa)
        else:
            print(f"Congrats, {player}. You have moved on to level two, where your fate will be determined randomly. Good luck.")
            print("\U0001f600")
            levelone_pointsb = points +5
            print(f"Current Points: {levelone_pointsb}")
            leveltwo(levelone_pointsb)
    
def leveltwo(leveltwo_points: int) -> None:
    print("Now you are randomly assigned a fate")
    from random import randint
    fate = int = randint(1,2)
    if fate == 1:
        print(f"Sorry, {player}. You lose. Goodbye, {player}")
        print(f"Final Points: {leveltwo_points}")
        playagain()
    else:
        print(f"You Win! Congrats {player}!! You are a master at the Random Game.")
        print("\U0001f600")
        leveltwo_pointsb = leveltwo_points + 10
        print("Final Points:")
        print(leveltwo_pointsb)
        
if __name__ == "__main__":
  main()
