"""
Greek Wordle Game in Python

Author: NicknamedXD
Date: 12/31/2023
Description: Basic version of the game wordle made in python containing all greek words.It features two difficulties and does not require any external libraby,made as an assignment for uni .
"""


from random import choice      #imports only choice to save space.

def select_difficulty():                    #function that determines difficulty.
    difficulty = input("Enter 'H' or 'h' for hard mode, or any other input for normal mode: ")
    return "hard" if difficulty.lower() == "h" else "normal"

def dikse_feedback(guess, word): # feed back calculation (takes into account multiple instances of letters in word and guess).
    feedback=["-","-","-","-","-"]  #guess starts as ----- and just adds x and o's.
    lexi=list(word)  
    for i in range(len(word)):
        if word[i]==guess[i]: 
            feedback[i]="O" #adds the O.
            lexi.remove(guess[i])
    for i in range(len(word)):  
        if guess[i] in lexi:
            feedback[i]="X" #adds the X.
            lexi.remove(guess[i])
    return "".join(feedback)
def add_to_set(guess, guessed, word):       #adds letters to the guessed set ( used in the hard difficulty).
    guessed.update(letter for letter in guess if letter not in word)

words = [line.strip() for line in open("5letterwords.txt", "r", encoding="utf-8")]     #opens file with utf-8 in readmode and strps every line and adds it to words in order to get all the words.

level = select_difficulty()                         #uses the functin to select the difficulty.
word =choice(words)                            #selects random word from the list of words.
guessed = set()                     #declaring set for the guessed letters to be added.
letters = set()               # calculated the letters since turnin dosent accept greek .
for code in range(913, 938):
    letters.add(chr(code))
letters.remove('\u03a2') #removes \u03a2 becouse its a symbol.
    
i = 0   # declaring the i because its needed to start the main program loop.

while i < 6:                                                                        #main loop
    guess = input(f"Please enter your guess no {i+1}: ").upper() #takes guess.

    if len(guess) != 5: #checks if its 5 letters
        print("Word is not 5 letters, try again.")
        continue

    used = {letter for letter in guess if letter in guessed}     #checks for already used letters in the hard difficulty
    
    if level == "hard" and used:
        print(f"Cannot use letters {used} known not to exist in word.")
        continue

    if guess not in words :      #asks for guess again if guess not in dictionary.
        print("Not a valid word in my dictionary. Try again.")
        continue



    add_to_set(guess, guessed, word)            #adds guessed letters to sed for the hard difficulty.
    feedback = dikse_feedback(guess, word)              #call for the calculation of feedback and prints it.
    print(feedback)

    if feedback == "OOOOO":
        print(f"SUCCESS: you found the secret word in {i+1} tries")     #checks if the word has been found and ends the loop .
        break

    print(f"Letters not in secret word: {guessed}\nLetters that may be in secret word: {letters - guessed}")  # both prints in one line .

    i += 1 #adds one to i so the loop is not infinite

if i == 6:
    print("You failed to find the secret word in 6 tries.")      #gameover screen.
    print(f"The secret word was {word}")

