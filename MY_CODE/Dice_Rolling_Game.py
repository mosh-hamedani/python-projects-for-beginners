# Loop
    # Ask the user: roll the dice (y/n)
    # If user generate y
    #   generate two numbers
    #   print them
    # If user generate n
    #   thank you message
    #   Terminate
    # Else
    #   print error message

import random

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1, 6)
        return first, second
    
while True:
    choice = input('Roll the dice? (y/n): ').lower()
    if choice == 'y':
        dice = Dice()
        print(dice.roll())

    elif choice == 'n':
        print("Thanks for playing!")
        break

    else:
        print('INVALID KEYWORD')