# Loop
    # generate a random number
    # ask user to make a guess
    # if not valid
    #   print error message
    # if number < guess
    #   print too low
    # if number > guess
    #   print too high

import random


number_to_guess = random.randint(1, 100)

while True:

    try:

        guess = int(input('Guess a number between 1-100: '))

        if guess < number_to_guess:
            print('Too low!')
        elif guess > number_to_guess:
            print('Too High!')
        else:
            print('Congrats! You guessed the number!')
            break

    except ValueError:
        print('Please input a valid number.')

        
