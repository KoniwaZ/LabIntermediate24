word = "Prasmul".lower()
guess = ["_"] * len(word)
complete = False

for char in guess:
    print(char, end=" ")
print()


while complete != True:
    guessing = input("Type one character: ").lower()
    
    if guessing in word:
        for i in range(len(word)):
            if word[i] == guessing:  
                guess[i] = guessing
                print("You right! Continue guessing")
        
        for char in guess:
            print(char, end=" ")
        print()
        
        if "_" not in guess:
            print("Completed! The word is :", word)
            complete = True
    else:
        print("Wrong. Guess another character.")
