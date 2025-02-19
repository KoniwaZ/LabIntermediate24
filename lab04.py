import random

def main():
    global guess, guessed, score, word, words

    words = ["prasmul", "qwert", "parkir"]
    score = 0

    while words:  # Keep playing until all words are guessed
        word = random.choice(words).lower()
        chance = len(word)+2
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
            nonlocal chance
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
                chance -= 1
                print(f"Wrong guess. You have life {chance} left.")

            return False

        # Word guessing loop
        while "_" in guess and chance>0:
            for char in guess:
                print(char, end=" ")
            print()
            print(f"You have {chance} chances left. Your current score is: {score}")
            while True:
                guessing = input("Type one character (or 'quit' to exit): ").lower()
                if guessing == "quit":
                    print(f"You quit the game. Final Score: {score}")
                    return  
                if guessing.isalpha() and len(guessing) == 1:
                    break
                print("Invalid input! Please enter a single letter.")

            print(f"You have {chance} chances left. Your current score is: {score}")

            if check_answer(guessing):  
                break
            
        if chance == 0:
            print(f"You ran out of chances! The word was: {word}")
    # End of game
    print(f"Game over! You guessed all words. Final Score: {score}")

# Run the game
main()
