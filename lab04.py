import random

def main():
    global guess, guessed, score, word, words  

    words = ["prasmul", "qwert", "parkir"]
    score = 0

    while words:  # Keep playing until all words are guessed
        word = random.choice(words).lower()
        guess = ["_"] * len(word)
        guessed = []

        def check_word(guessing):
            #Check if the letter was already guessed
            if guessing in guessed:
                print(f"You already guessed '{guessing}'. Try another one.")
                return False
            guessed.append(guessing)
            return True

        def update_guess(guessing):
            #Update the guessed word array
            for i in range(len(word)):
                if word[i] == guessing:
                    guess[i] = guessing

        def calculate_score():
            #add score
            global score
            score += 1

        def check_answer(guessing):
            #Check if the guessed letter is correct
            if not check_word(guessing):
                return  #wrong asw

            if guessing in word:
                update_guess(guessing)
                print("Correct guess!")

                if "_" not in guess:  # If the word is completely guessed
                    calculate_score()
                    print(f"Congratulations! You guessed the word: {word}")
                    print(f"Your current score is: {score}\n")
                    words.remove(word)
                    return True
            else:
                print("Wrong guess.")

            return False

        # Word guessing loop
        while "_" in guess:
            for char in guess:
                print(char, end=" ")
            print()
            guessing = input("Type one character (or 'quit' to exit): ").lower()

            if guessing == "quit":  # Exit if user types 'quit'
                print(f"You quit the game. Final Score: {score}")
                return

            if check_answer(guessing):  
                break

    # End of game
    print(f"Game over! You guessed all words. Final Score: {score}")

# Run the game
main()
