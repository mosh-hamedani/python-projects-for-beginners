# Guess a number between 1 to 100
# Secret number
# guess count

import range


guess_count = 0
#guess_limit = 0
secret_number = 8

while guess_count:
    guess = int(input('Guess a number between 1-100: '))
    
    if guess > secret_number:
        print('Too High!')

    elif guess < secret_number:
        print('Too Low!')

    elif guess == secret_number:
        print('Congratulations! You guessed the number!')

        break

else:
    print('Please put a valid number')
