#!/bin/python3

import logging

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')  # ? this is the configuration for the debuging.
logging.basicConfig(filename='myProgramLogs.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')  # ? it will print the log messages in a new or selected text file
# logging.disable(logging.CRITICAL)  # ? this program disable all the logging messages, insted of comment them.


logging.debug('Start of program')

def factorial (n):
  logging.debug('Start of factorial (%s)' % (n))  # %s stands for: substitution, and then we have the % (n) which stands for the variables than will be exchanged.
  total = 1
  for i in range (1, n + 1):
    total *= i
    logging.debug('i is %s, total is %s' % (i, total))

  logging.debug('Return value is %s ' % (total))
  return total

print(factorial(5))

logging.debug('End of program')