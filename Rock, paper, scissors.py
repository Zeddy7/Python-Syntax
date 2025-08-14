import random
choices = ('rock', 'paper', 'scissors')
while True:
    ask = input('Start or exit: ').lower()
    if ask == 'start':
      user = input('Choose rock, paper or scisors: ').lower()
      computer = random.choice(choices)
      if user == computer:
        print('Tie')
      elif (user == 'rock' and computer == 'scissors') or (user == 'paper' and computer == 'rock') or (user == 'scissors' and computer == 'paper'):
        print('You won')
      elif user != 'rock' or 'paper' or 'scissors':
        print('Invalid')
        continue
      else:
        print('You lost')
      print('Computer chose:',computer)
    elif ask == 'exit':
      break
    else:
      print('Invalid ')

print('Thanks for playing')