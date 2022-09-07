#!/usr/bin/python3

import re  # import the regulax expresion options


beginsWithRegex = re.compile(r'Hello')  # ? this will match just if the string starts with 'Hello'
result = beginsWithRegex.search('Hello there !')
print(result.group())


endsWithRegex = re.compile(r'World!$')  # ? this will match just if the string ends with 'World!'
answ = endsWithRegex.search('what is new in the World!')
print(answ.group())


allDigitsRegex = re.compile(r'^\d+$')  # ? starts with 1 or more digits and also finish with 1 or more digits
answ = allDigitsRegex.search('1234365324576')
answ2 = allDigitsRegex.search('1234x987')  # this does not match the the regex above
print(answ.group())
print(answ2)  # == None