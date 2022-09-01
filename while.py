
      # ? While loops

spam = 0
while spam < 5:
  print('Hello World')
  spam += 1


name = ''
while name != 'your name':
  print ('Please enter your name')
  name = input()
print('Thank you !!!')


name = ''
while True:  # it is a truethy statement so it will never be false, this is an "infitive" loop
  print('Please type your name.')
  name = input()
  if name == 'your name':
    break  # with break we can exit the infinitve loop
print('Thank you again !!')


spam = 0 
while spam < 5:
  spam += 1
  if spam == 3:
    continue  # this will make the program "jump" when the 3 is reached.
  print('spam is ' + str(spam))