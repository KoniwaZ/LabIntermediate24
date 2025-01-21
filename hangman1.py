wordU = "Prasmul"
word = wordU.lower()
guess = []
complete = False
i = 0

while complete != True:
    guessingU = input("Type one character ")
    guessing = guessingU.lower()
    if guessing == word[i] :
        guess.append(guessing)
        i = i+1
        print("You right! Continue guessing")
        if len(guess) == len(word):
            print("Completed")
            break
    else :
        print("Wrong. Guess another character")