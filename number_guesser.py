import random

print("Hello and welcome to my number guessing game!")
count = 0
playing = input("Do you want to play?\nYes or No : ").lower()

if playing == "yes":
    playing = True
else:
    playing = False

while playing:
    ub = input("Enter upper bound: ")
    if ub.isdigit():
        ub = int(ub)
        if ub < 0:
            print("Enter a value greater than zero.")
            break
    else:
        print("Enter int as value.")
        break
    x = random.randint(0, ub)
    answer = input("Enter your answer: ")
    if answer.isdigit():
        answer = int(answer)
        count+=1
    else:
        print("Enter int as value.")
    
    while answer != x:
        if answer > x:
            print("Your are HIGHER than the required answer")
            answer = input("Enter your answer: ")
            if answer.isdigit():
                answer = int(answer)
                count+=1
            else:
                print("Enter int as value.")
        if answer < x:
            print("Your are LOWER than the required answer")
            answer = input("Enter your answer: ")
            if answer.isdigit():
                answer = int(answer)
                count+=1
            else:
                print("Enter int as value.")
    
    print("You got the correct answer!")
    print(f"It took you {count} tries to get the correct answer.")
    count = 0
    playing = input("Do you want to play again?\nYes or No : ").lower()
    if playing == "yes":
        playing = True
    else:
        playing = False

print("\nGame over")
print("The End.")

