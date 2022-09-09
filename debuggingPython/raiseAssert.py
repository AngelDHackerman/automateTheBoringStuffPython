#!/bin/python3

'''
************
*          *
*          *
*          *
************
'''

def boxPrint (symbol, width, height ):

  if len(symbol) != 1:
    raise Exception('"symbol" needs to be a string of length 1')  # * raise will throw and error message if the condition is true.
  
  if width < 2 or height < 2:
    raise Exception('"width" and "height" must be greater or equal to 2')


  print(symbol * width)  # ? prints the top side of the box

  for i in range (height - 2):
    print(symbol + ( ' ' * (width - 2)) + symbol)  # ? prints the inside part of the box

  print(symbol * width)  # ? prints the bottom of the box


boxPrint('*', 15, 10)
boxPrint('O', 15, 7)

# this will cause a bug:
# boxPrint('**', 10, 4)
# boxPrint('U', 1, 1)