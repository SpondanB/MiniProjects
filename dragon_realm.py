import random
import time

def intro():
    print("You are in a land full of dragons.") 
    print("In front of you, you see two caves.") 
    print("In one cave, the dragon is friendly and will share his treasure with you.")
    print("The other dragon is greedy and hungry, and will eat you on sight.")

def choose_cave():
    while True:
        chosencave = input("Which cave will you chose to enter? (1 or 2): ").strip()
        if chosencave.isdigit() and int(chosencave) in (1,2):
            chosencave = int(chosencave)
            return chosencave
        else:
            print("Enter a proper cave number.")


def checkcave(chosencave):
    print("You approach the cave...")
    time.sleep(2)
    print("It is dark and spooky...")
    time.sleep(2)
    print("A large dragon jumps out in front of you! He opens his jaws and...")
    time.sleep(2)
    safecave = random.randint(1, 2)
    if safecave == chosencave:
        print("Gives you his treasure!")
    else:
        print("Gobbles you down in one bite!")

while True:
    intro()
    selectedcave = choose_cave()
    checkcave(selectedcave)
    play = input("Do you want to play again? (Y/N): ").lower().strip()
    if play != "y":
        break

print("Game over.")



