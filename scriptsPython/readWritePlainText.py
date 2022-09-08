#!/usr/bin/python3 

      # ! Reading a file

helloFile = open('./text.txt', 'r')  # ? open a file in the read mode
print(helloFile.read())  # ? read method will read the file and then you can print it

helloFile.close()  # ? in this way you will close the file



      # ! readlines method

