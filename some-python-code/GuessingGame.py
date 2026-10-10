# Guessing game
import random

guesses = 0
secret_number = random.randint(1, 21)
guessed = False
user_response = '' 
max_attempts = 4

while guesses < max_attempts:
    print('Guesses left: '+str(guesses)+'/4')
    try:
        user_response = int(input("Enter a guess: "))
    except ValueError:
        print("Please enter numbers only")
        continue
    if user_response == secret_number:
        guessed = True
        break

    if user_response > secret_number:
        print("Your guess is too high.")
        guesses += 1
    elif user_response < secret_number:
        print("Your guess is too low.")
        guesses += 1

if guessed:
    print("Your good at guessing! The number that I was thinking of was "+str(secret_number))
    
else:
    print('Guesses left: '+str(guesses)+'/4')
    print("Unfortunately, You ran out of guesses. Better try well next time :)")
