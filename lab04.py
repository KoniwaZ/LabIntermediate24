def main(word):
    word = word
    guess = ["_"] * len(word)
    guessed = []
    chance = len(word) + 2
    while chance > 0:
        for char in guess:
            print(char, end=" ")
        print()
        print("Chance left:", chance)
        guessing = input("Type one character: ").lower()
        alpha = guessing.isalpha()
        if alpha == True :
            if guessing in guessed:
                print("You already guessed this character. Try another one.")
                continue
            else:
                guessed.append(guessing)
            
            if guessing in word:
                chance -= 1
                for i in range(len(word)):
                    if word[i] == guessing:  
                        guess[i] = guessing
                
                print(f"Congrats, {guessing} is in the secret word!")
                
                if "_" not in guess:
                    print("Completed! The secret word is :", word)
                    break
            else:
                chance -= 1
                if chance > 0:
                    print(f"Wrong. {guessing} is not in the secret word. Guess another character.")
                else:
                    print("You lose, out of chance. The secret word is :", word)
                    break
        else :
            print("Invalid input. Try again.")

main(input("Enter the secret word: ").lower())