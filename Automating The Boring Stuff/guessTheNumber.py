# This is a guess the number game.

import random
secreatNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secreatNumber:
        print('Your guses is too low.')
    elif guess > secreatNumber:
        print('Your guess is too high')
    else:
        break  # This condition is the correct guess!

if guess == secreatNumber:
    print('Good Job! You guessed my number in '+str(guessesTaken)+' guesses!')
else:
    print('Nope. The number I was thinking of was '+ str(secreatNumber))
        
