#!/usr/bin/python3

import re 

atRegex = re.compile(r'.at')  # ? anything followed by 'at'

answ = atRegex.findall('the cat in the hat sat on the flat mat')
print(answ)  # ['cat', 'hat', 'sat', 'lat', 'mat']  pay attention to 'lat' which was 'flat' in the original string



atRegex = re.compile(r'.{1,2}at')  # ? 1 or 2 character followed by 'at'

answ = atRegex.findall('the cat in the hat sat on the flat mat')
print(answ)  # [' cat', ' hat', ' sat', 'flat', ' mat'] now it shows 'flat' as in the string but it also pics the space before the word