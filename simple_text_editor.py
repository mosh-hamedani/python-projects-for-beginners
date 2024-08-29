import os

def read_file(filename):
  with open(filename, 'r') as file:
    return file.read()
  
def write_file(filename, content):
  with open(filename, 'w') as file:
    file.write(content)


def get_user_input():
  print('\nEnter your text (type SAVE on a new line to save and exist):')
  
  lines = []
  while True:
    line = input()
    if line == 'SAVE':
      break
    lines.append(line)  
  
  return '\n'.join(lines)

def main():
  filename = input('Enter the filename to open or create: ').strip()
  try:
    if os.path.exists(filename):
      print(read_file(filename))
    else:
      write_file(filename, '')
 
    content = get_user_input()
    write_file(filename, content)
    print(f'{filename} saved.')
  except OSError:
    print(f'{filename} could not be opened.')

if __name__ == '__main__':
  main()