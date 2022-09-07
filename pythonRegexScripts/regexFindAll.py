#!/usr/bin/python3

import re

print('\n\t Match a all the phone numbers: \n')
      # ! regex for match all the phone numbers: 

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

resume = '''
508-555-5555   asdfoiqwerm as;ldkf ow. zxcovsaa 508-555-1234
'''

result = phoneRegex.findall(resume)  # ? findall() will show you all the matches of the regex.
print(result)  # this one returns a array 

phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
result = phoneRegex.findall(resume)
print(result)  # this one returns tuples.



print('\n\t Match all the numbers followed byt a string: \n')

      # ! Regex for match a number followed by a string:

lyrics = ' 12 aosiudf  , 11 laksdfoimx.c,vjops, 10 qpo imxlckvjoasmdf, 9 lalasiwedflaiwsdf, 8 lkmv,zxmcvm.,.,sxacvmkvm, 7 oqieinvm.z,xcmvopiajfvcmk, 6 qiiweirjwfsl,dfm, 5 kasmv,mzx/c,.vmz/x.,cvm, 4 qoierfuwiejflaskjdf.jvaiksdf 3 akifwjeoifkmalskdfj 2 olikwjeoifjalskdfjl 1 lkasjdfoiqwmef '


xmasRegex = re.compile(r'\d+\s\w+')  # ? \d+ : one or more digits; \s : means that there will be a space; \w+ : then followed by one or more words

print(xmasRegex.findall(lyrics))