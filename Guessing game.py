#Creating secret number for user to guess
secret_num = 9
tries = 0
while tries < 3: #user has only 3 guesses
  player_guess = int(input('Guess: '))
  tries += 1 #guess goes up by one so as to avoid infinite loop
  if player_guess == secret_num: #if the user guesses the secret number, they win and the game ends.
    print('You won')
    break
else:
  print('You lost') #If the user never guesses the secret number, the game ends and the user loses.