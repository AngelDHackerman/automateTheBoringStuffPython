#!/bin/python3

helloFile = open('./text.txt')

print(helloFile.readlines())  # ? this will retunr a array with all the lines in the file

helloFile.close()