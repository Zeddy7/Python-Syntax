import random


secret = random.randint(1, 101)


while True:
  ask = input('S to start game and Q to end game: ').upper()
  if ask == 'S':
    for i in range(3):
      try:
        Guess = int(input('Guess a number between 1 and 100: '))
      except:
        print('Invalid value')
      if Guess == secret:
        print('You win')
        break
      elif Guess > secret:
          print('Too high')
      else:
          print('Too low')
    else:
      print('You lost')
  elif ask == 'Q':
      break
  else:
    print('Invalid')
    continue


print('Thanks for playing')
