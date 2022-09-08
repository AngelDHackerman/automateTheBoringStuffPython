#!/bin/python3

import os

helloFile = open('./text2.txt', 'w')  # ? 'w' for write and 'a' for append text to the file

helloFile.write('Helloooooooooooo \n')
helloFile.write('Helloooooooooooo \n')
helloFile.write('Helloooooooooooo \n')
helloFile.write('Helloooooooooooo \n')

helloFile.close()



baconFile = open('./bacon.txt', 'w')  # ? write a new document
baconFile.write('Bacon is not a vegetable.')

baconFile.close()

baconFile = open('./bacon.txt', 'a')  # ? append text to the document
baconFile.write('\n\nalso it is delicious.')



