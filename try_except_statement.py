
def div42by(dividedBy):
  try:
    return 42 / dividedBy
  except ZeroDivisionError:
    print('Error: You tried to divide by Zero.')

print(div42by(2))
print(div42by(12))
print(div42by(0))  # this will make an error
print(div42by(4))


print('How many cats do you have?')
num_cats = input()
try:
  if int(num_cats) >= 4:
    print('Thats a lot of cats !!!')
  else:
    print('That is not too many cats')
except ValueError:
  print('That is not a valid number')