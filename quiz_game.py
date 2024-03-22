print("Hello and welcome to my quiz!")
count = 0
playing = input("Do you want to play?\nYes or No : ").lower()

if playing != "yes":
    pass
else:
    print("OK then lets play :)\n")
        
    print("\nWho painted the Mona Lisa? \na) Leonardo da Vinci\nb) Michelangelo")
    ans = input("Answer(a or b): ")
    if ans.lower() == "a":
        count+=1
        print("Correct!")
    else:
        print("Wrong!")
    print("\nWho wrote the play 'Romeo and Juliet'?\na) William Shakespeare\nb) Jane Austen")
    ans = input("Answer(a or b): ")
    if ans.lower() == "a":
        count+=1
        print("Correct!")
    else:
        print("Wrong!")
    print("\nWhat is the capital city of Australia?\na) Sydney\nb) Canberra")
    ans = input("Answer(a or b): ")
    if ans.lower() == "b":
        count+=1
        print("Correct!")
    else:
        print("Wrong!")
    print("\nWhat is the largest planet in our solar system?\na) Jupiter\nb) Saturn")
    ans = input("Answer(a or b): ")
    if ans.lower() == "a":
        count+=1
        print("Correct!")
    else:
        print("Wrong!")
    print("\nWhat is the chemical symbol for gold?\na) Ag\nb) Au")
    ans = input("Answer(a or b): ")
    if ans.lower() == "b":
        count+=1
        print("Correct!")
    else:
        print("Wrong!")
    
    print(f"\nYour score is: {count}/5")
    print(f"You got {(count/5)*100}%")

print("\nThe end.")