#!/usr/bin/python3

import re

print('\n\t Making your own character classes: \n')
lorem = ''' Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'''

vowerlRegex = re.compile(r'[aeiouAEIOU]')  # ? is the same like: r'a|e|i|o|u|A|E|I|O|U'
print(vowerlRegex.findall(lorem))


print('\n')

doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')  # ? this will return just where they are 2 vowels together.
print(doubleVowelRegex.findall(lorem))


print('\n')

revertVowelRegex = re.compile(r'[^aeiouAEIOU]')  # ! the ^ indicates to the oposite of the regex above (it will match constans and numbers, etc.)
print(revertVowelRegex.findall(lorem))