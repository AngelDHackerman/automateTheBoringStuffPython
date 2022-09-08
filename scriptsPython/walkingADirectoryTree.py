#!/bin/python3

from fileinput import filename
import os

# ? os.walk, returns 3 values and they must be used in a for loop like so:

for folderName, subFolders, fileNames in os.walk('../testDirectory'):
  # pass
  print(f'The folder is {folderName}')
  print(f'The sub-folders in {folderName} are: {str(subFolders)}')
  print(f'The file names in {folderName} are: {str(fileNames)}')
  print('\n')

