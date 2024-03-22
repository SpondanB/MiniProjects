import random

print("Hello and welcome to my hangman game!")

words =  'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep  snake spider stork swan tiger'.split()
hangman = ['''
  +---+
      |
      |
      |
  ====''', '''
  +---+
   O  |
      |
      |
  ====''', '''
  +---+
   O  |
   |  |
      |
  ====''', '''
  +---+
   O  |
  /|  |
      |
  ====''', '''
  +---+
   O  |
  /|\ |
      |
  ====''', '''
  +---+
   O  |
  /|\ |
  /   |
  ====''', '''
  +---+
   O  |
  /|\ |
  / \ |
  ====''']

playing = input("Do you want to play?\nYes or No : ").strip().lower()

if playing == "y":
    playing = True
elif playing == "yes":
    playing = True
else:
    playing = False
while playing:
    print("\nH A N G M A N\n")
    word = random.choice(words)
    correct_word = ""
    letters_not_present = ""
    text_on_screen = ""
    guesses = []
    correct_guesses = []
    count = 0
    
    for i in word:
        correct_guesses.append(i)
    
    for i in word:
        text_on_screen += "_ "
        correct_word += i+" "
    
    
    while True:
        print()
        print(hangman[count])
        print("Leters that are not present: "+letters_not_present)
        print(text_on_screen)
        ans_char = input("Make a guess: ").strip().lower()
        if ans_char not in guesses:
            guesses.append(ans_char)
        else:
            print("you already guess that.")
            continue
        if ans_char in correct_guesses:
            text_on_screen = ""
            for i in word:
                if i in guesses:
                    text_on_screen += i+" "
                else:
                    text_on_screen += "_ "
        else:
            letters_not_present += ans_char+" "
            count+=1
        if text_on_screen == correct_word:
            print()
            print("Yes the secret word is "+word+".")
            print("You won")
            break
        elif count > 6:
            print("You have run out of guess.")
            print("You lost")
            break
    playing = input("Do you want to continue playing?\nYes or No : ").strip().lower()
    if playing == "y":
        playing = True
    elif playing == "yes":
        playing = True
    else:
        playing = False

print("\nGame over")
print("The End.")

    
    
    