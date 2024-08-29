import random 

def roll_die():
  return random.randint(1, 6)

def play_turn(player_name):
  turn_score = 0

  print(f"\n{player_name}'s turn")

  while True:
    roll = roll_die()
    print(f'You rolled a {roll}')

    if roll == 1:
      return 0
    
    turn_score += roll
    choice = input('Roll again? (y/n): ').lower()
    if choice != 'y':
      return turn_score


def main():
  scores = [0, 0]
  current_player = 0 

  while True:
    player_name = f'Player {current_player + 1}'
    turn_score = play_turn(player_name)
    scores[current_player] += turn_score

    print(f'\nYou scored {turn_score} points this turn.')
    print(f'Current scores: Player 1: {scores[0]}, Player 2: {scores[1]}')

    if scores[current_player] >= 100:
      print(f'{player_name} wins!')
      break

    current_player = 1 if current_player == 0 else 0

if __name__ == '__main__':
  main()