import random

print("Hello and welcome to my rock paper scissors game!")
comp = 0
player = 0
option = ['r', 'p', 's']
playing = input("Do you want to play?\nYes or No : ").strip().lower()

if playing == "yes":
    playing = True
else:
    playing = False

while playing:
    x = random.choice(option)
    choice = input ("Rock(R)\nPaper(P)\nScissors(S)\nYour selection: ").strip().lower()
    if choice not in option:
        print("Enter valid input next time.")
        break
    
    print("Computer's selection: "+x)
    x = option.index(x)
    y = option.index(choice)
    if y == (x+1)%3:
        player += 1
        print(f"Player: {player}\tComputer: {comp}")
    elif x == (y+1)%3:
        comp += 1
        print(f"Player: {player}\tComputer: {comp}")
    else:
        print(f"Player: {player}\tComputer: {comp}")
    
    playing = input("Do you want to play again?\nYes or No : ").strip().lower()
    if playing == "yes":
        playing = True
    else:
        playing = False

print("\nGame over")
print("The End.")

    







