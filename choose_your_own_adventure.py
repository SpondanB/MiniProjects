endings = [0, 0, 0, 0, 0]
print("Hello and welcome to my choose your own adventure game!")
count = 0
playing = input("Do you want to play?\nYes or No : ").strip().lower()

if playing == "yes":
    playing = True
else:
    playing = False

while playing:
    print("\nYou find yourself standing in a forest trail surrounded by towering trees and the sound of rustling leaves. The path eventually splits into two.")
    print("You can take the left or the right path... ")
    while True:
        choice = input("Enter 'left' to take the left path.\nEnter 'right' to take the right path.\nEnter your choice: ").strip().lower()
        if choice == "left" or choice == "right":
            print("-----------------------------------")
            break
        else:
            print("Enter valid response.")
    if choice == "left":
        print("You move toward the left path.")
        print("You find on old chest on the side of the trail.\nYou can either open it or leave it alone.")
        while True:
            choice = input("Enter 'open' to open the chest.\nEnter 'leave' to ignore the chest.\nEnter your choice: ").strip().lower()
            if choice == "open" or choice == "leave":
                print("-----------------------------------")
                break
            else:
                print("Enter valid response.")
        if choice == "open":
            print("You opened the chest.")
            print("It contains a haunted doll which posesses you and gives you a gruesome death")
            print("\nBAD END")
            endings[0] = 1
            for i in endings:
                if i == 1:
                    count+=1
            print(f"You found {count} endings")
        else:
            print("You left the chest and went ahead.")
            print("You find a dark and gloomy lake in front of you.\nYou can either swim through it or walk arround it.")
            while True:
                choice = input("Enter 'swim' to swim through the lake.\nEnter 'walk' to walk arround the lake.\nEnter your choice: ").strip().lower()
                if choice == "swim" or choice == "walk":
                    print("-----------------------------------")
                    break
                else:
                    print("Enter valid response.")
            if choice == "swim":
                print("You started to swim accross.")
                print("But alas you forgot you dont know how to swim.")
                print("You start to drown. The suddenly a monstrous fish comes and eats you up.")
                print("\nUNFORTUNATE END")
                endings[1] = 1
                for i in endings:
                    if i == 1:
                        count+=1
                print(f"You found {count} endings")
            else:
                print("You started to walk arround the lake.")
                print("Accross the lake you found a road taking you to the nearest town.")
                print("In that town you live happily ever after.")
                print("\nOKAY END")
                endings[2] = 1
                for i in endings:
                    if i == 1:
                        count+=1
                print(f"You found {count} endings")
    else:
        print("You move toward the right path.")
        print("You came accross a  mountainous region. Here you can prominently see a cave on the side of the mountain.")
        print("You can either enter it or leave it alone and move forward.")
        while True:
            choice = input("Enter 'enter' to enter the cave.\nEnter 'leave' to ignore the cave.\nEnter your choice: ").strip().lower()
            if choice == "enter" or choice == "leave":
                print("-----------------------------------")
                break
            else:
                print("Enter valid response.")
        if choice == "enter":
            print("You enter the cave to seek shelter for the night.")
            print("But sadly the cave was the home of couple of mountain lions who took your intrusion very poorly.")
            print("You are torn apart limb-to-limb and then you die")
            print("\nWILD END")
            endings[3] = 1
            for i in endings:
                if i == 1:
                    count+=1
            print(f"You found {count} endings")
        else:
            print("You leave the cave and walk ahead.")
            print("On the bushes you find a teleporter, using which you can travel.")
            print("You spend rest of your life traveling all over the world lliving an awesome life.")
            print("\nAWESOME END")
            endings[4] = 1
            for i in endings:
                if i == 1:
                    count+=1
            print(f"You found {count} endings")    
    count = 0
    playing = input("Do you want to continue playing?\nYes or No : ").strip().lower()
    if playing == "yes":
        playing = True
    else:
        playing = False

print("\nGame over")
print("The End.")
