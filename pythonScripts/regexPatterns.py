#!/usr/bin/python3
import re

      # ! Matching 0 or 1 times ?

print('\n\t Match 0 or 1 times:')
batRegex = re.compile(r'Bat(wo)?man')  # ? the ? states that pattern appears 1 or 0 times

matchObject = batRegex.search('The aventures of Batman')
print(matchObject.group())  # in here it appeares 0 times

matchObject = batRegex.search('The aventures of Batwoman')
print(matchObject.group())  # in here it appeares 1 time

matchObject = batRegex.search('The aventures of Batwowowowoman')
print(matchObject)  # None == because it matches more than 1 time.


#todo: This one will match if has or not an area code. 

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')  
matchObject = phoneRegex.search('My phone number is 415-555-3334. Call me now')
print(matchObject.group())

matchObject = phoneRegex.search('My phone number is 555-3334. Call me now')
print(matchObject.group())



print('\n\t Matches 0 or more times:')

      # ! Matching 0 or more times *

batRegex = re.compile(r'Bat(wo)*man')
matchObject = batRegex.search('The aventures of Batman')
print(matchObject.group())  # Matches 0 times

matchObject = batRegex.search('The aventures of Batwoman')
print(matchObject.group())  # matches 1 time

matchObject = batRegex.search('The aventures of Batwowowowoman')
print(matchObject.group())  # matches several times.



print('\n\t Matches 1 or more times')

      # ! Matching 1 or more times +

