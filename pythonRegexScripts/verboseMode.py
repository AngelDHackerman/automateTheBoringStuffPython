#!/usr/bin/python3

import re

phoneRegex = re.compile(r'''
\d\d\d  # area code 
-       # first dash
\d\d\d  # first 3 digits
-       # second dash
\d\d\d\d  # last 4 digits
''', re.VERBOSE)  # ? the VERBOSE option allows the regex to be more readable just like the example above.

rst = phoneRegex.findall('555-999-4545 as qwioerukasdfu 999-888-1010 ')
print(rst)  # ['555-999-4545', '999-888-1010']



phoneRegex = re.compile(r'''
\d\d\d   
-
\d\d\d
-
\d\d\d\d
''', re.IGNORECASE | re.DOTALL | re.VERBOSE)  # ? you can combine several regex methods using the BITWISE or pipe | operator.