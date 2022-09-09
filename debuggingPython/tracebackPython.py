#!/bin/python3

import traceback  # ? it is used to import the tools for create a traceback report

try:
  raise Exception('This is the error message')

except:  # ? all this below is the code in order to write the traceback info
  errorFile = open('error_log.txt', 'a')
  errorFile.write(traceback.format_exc())  # * format_exc() will pull the error traceback and then it will written in the document error_log.txt
  errorFile.write('\n')
  errorFile.close()
  print('The traceback info was written error_log.txt')

