#!/usr/bin/python3

import re
textSample = '''Lorem Ipsum is simply Agent Maravilla industry. Lorem Ipsum has been the industry's Agent 007 dummy text Agent Aldus PageMaker including versions of Lorem'''

print ('\n\t ')
      # ! Find a word:

namesRegex = re.compile(r'Agent \w+')  # ? find the word 'Agent' followed by 1 or more words 
rst = namesRegex.findall(textSample)
print(rst)


print ('\n\t ')
      # ! Find a replace: 

rst = namesRegex.sub('REDACTED', textSample)  # ? the .sub method will replace the word found.
print(rst)


print ('\n\t ')
      # ! Find a initial and replace it:

namesRegex = re.compile(r'Agent (\w)\w*')  # the initial is store in the group 1
rst = namesRegex.findall(textSample)
print(rst)

rst = namesRegex.sub(r'Agent \1*****', textSample)  # ? \1 stands for: use the group 1 of the regex above
print(rst)
