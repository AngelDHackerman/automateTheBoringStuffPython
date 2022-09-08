#!/bin/python3

import shelve  # ? shelve is use to storage date, such as a DICTIONARY

shelfFile = shelve.open('myData')  # ? this is a new BINARY file were we'll store our data.
shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail', 'Cleo']  # ? the [keyValue] = ['values']
shelfFile.close()

  # this is how we print the data stored before:

shelfFile = shelve.open('myData')
print(shelfFile['cats'])
shelfFile.close()