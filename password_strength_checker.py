import re

def check_password_strength(password):
  strength = 0 

  if len(password) >= 8:
    strength += 1
  if re.search('[a-z]', password):
    strength += 1
  if re.search('[A-Z]', password):
    strength += 1
  if re.search('[0-9]', password):
    strength += 1
  if re.search('[@#$%+=!]', password):
    strength += 1

  return strength
  

def main():
  password = input('Enter a password: ')
  strength = check_password_strength(password)

  if strength == 5:
    print('Password strength: Very Strong')
  elif strength == 4:
    print('Password strength: Strong')
  elif strength == 3:
    print('Password strength: Medium')
  elif strength == 2:
    print('Password strength: Weak')
  else:
    print('Password strength: Very Weak')




if __name__ == '__main__':
  main()