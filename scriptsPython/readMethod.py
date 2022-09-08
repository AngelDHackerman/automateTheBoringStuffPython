#!/usr/bin/python3 

print('\n\t read method:' )
      # ! Reading a file

helloFile = open('./text.txt')  # ? open a file in the read mode
print(helloFile.read())  # ? read method will read the file and then you can print it


helloFile.close()  # ? in this way you will close the file