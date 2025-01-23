word = "pmbs".lower()
guess = ["_"] * len(word)
guessed = []
chance = 6

for char in guess:
    print(char, end=" ")
print()

while chance > 0:
    print("Chance left:", chance)
    guessing = input("Type one character: ").lower()
    
    if guessing in guessed:
        print("You already guessed this character. Try another one.")
        continue
    else:
        guessed.append(guessing)
    
    if guessing in word:
        for i in range(len(word)):
            if word[i] == guessing:  
                guess[i] = guessing
                print("You right! Continue guessing")
        
        for char in guess:
            print(char, end=" ")
        print()

        chance -= 1
        
        if "_" not in guess:
            print("Completed! The word is :", word)
            break
    else:
        print("Wrong. Guess another character.")
        chance -= 1
if chance == 0:
    print("You lose, out of chance. The word is :", word)