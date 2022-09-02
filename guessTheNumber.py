import random

# This is guess the number game.
print('Hello. What is your name? ')
name = input()
secretNumber = random.randint(1, 20)
print(f'Well {name} I\'m thinking of number between 1 and 20 ')  # ? asi se hace la interpolacion en python.

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
  print('Take a guess')
  guess = int(input())
  if guess < secretNumber:
    print('Your guess is too low.')
  elif guess > secretNumber:
    print('Your guess is too high')
  else:
    break  # ? this condition is the right guess

if guess == secretNumber:
  print(f'Good job {name}! You guessed my number in {guessesTaken} attemps !!!')
else:
  print(f'Nope. The number I was thinkning of was: {secretNumber}')
