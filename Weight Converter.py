weight = int(input('Weight: '))
user = input('(L)bs or (K)gs: ').lower()
if user == 'k':
  weight_lbs = weight / 0.45
  print(weight_lbs)
elif user == 'l':
  weight_kg = weight * 0.45
  print(weight_kg)