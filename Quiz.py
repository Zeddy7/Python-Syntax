best_sport = 'Football'
best_subject = 'Math'
favourite_hobby = 'Coding'
guess_sport = input('What is my best sport: ')
guess_subject = input('What is my best subject: ')
guess_hobby = input('What is my favourite hobby: ')
score = 0
if guess_sport == best_sport:
  score += 50
  if guess_subject == best_subject:
    score += 50
    if guess_hobby == best_subject:
      score += 50


print(score)