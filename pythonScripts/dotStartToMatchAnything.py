#!/usr/bin/python3 

import re

text = 'First Name: Angel Last Name: Hernandez'

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')  # ? this will pick up the first and last name!
answ = nameRegex.findall(text)
print(answ)



      # ! (.*) is greedy; (.*?) is non-greedy

serve = '<To serve humans> for dinner.>'

nonGreedyRegex = re.compile(r'<(.*?)>')  # ? match anything between <> but little as possible  NON-GREEDY
print(nonGreedyRegex.findall(serve))


greedyRegex = re.compile(r'<(.*)>')  # ? match anything between <> as much as possible GREEDY
print(greedyRegex.findall(serve))



print('\n')

prime = 'Serve the public trust. \nProtect the innocent.\nUpload the law.'

dotStart = re.compile(r'.*')  # ? match anything except for new lines
result = dotStart.search(prime)
print(result.group())

print('\n')

      # ! DOTALL

dotStartAll = re.compile(r'.*', re.DOTALL)  # ? this will match anything even the new lines.
result = dotStartAll.search(prime)
print(result.group())