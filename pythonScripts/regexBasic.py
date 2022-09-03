#!/usr/bin/python3

import re  # ? este es el modulo para importar las expresiones regulares 

message = 'Call me 415-555-0000 tomorrow, or at 415-555-9999'

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d')  # * r'' stands for 'raw string'. and 'd' stands for digit.

# matchObjetc = phoneNumberRegex.search(message)  # * The regular expression data type has a 'search' method, it matches just 1 instances of the search
# print(matchObjetc.group())  # * group() will tell you the result

matchObjetc = phoneNumberRegex.findall(message)
print(matchObjetc)