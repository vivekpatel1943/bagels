import random 
NUM_DIGITS = 3
MAX_GUESSES = 20

def main():   #the main function

    while True: #main game loop
        secret_number = secretNumber()
        print("I have thought of a number.")
        print(f"You have {MAX_GUESSES} to guess it.")
        numGuesses = 1

        # 
        while numGuesses <= MAX_GUESSES:
            guess = ""
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{numGuesses}")
                guess = input("> ")
            
            clues = getClues(guess,secret_number)
            print(clues)
            numGuesses += 1

            if guess == secret_number:
                print("You got it.")
            elif numGuesses > MAX_GUESSES:
                print("sorry , you are out of guesses.")
                print(f"the secret number was {secret_number}")
            
        
        print("would you like to play again.")
        if not input("> ").startswith("y"):
            break
        else:
            continue


def secretNumber():
    allDigits = list("0123456789")
    random.shuffle(allDigits)
    secretNumber = ""
    for i in range(NUM_DIGITS):
        secretNumber = secretNumber +  allDigits[i]
    return secretNumber


def getClues(guess,secret_number):
    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            clues.append("fermi")
    
        elif guess[i] in secret_number:
           clues.append("pico")

    if len(clues) == 0:
        return "bagels"
    else:
        clues.sort()
        return " ".join(clues)

    return clues
        
if __name__== "__main__":
    main()
