#!/usr/bin/python3

import re 
import pyperclip  # ? you must install the pyperclip library, also you can check with pip freeze if it was installed correctly

# * Create a regex for phone numbers

phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?    # area code (optional), the ? indicates that is optional
(\s|-)                        # first separator, it can be an ' ' space or a dash -
\d\d\d                        # first 3 digits
-                             # separator
\d\d\d\d                      # last 4 digits
)
# (((ext(\.)?\s)|x)             # extension word-part (optional), it might be the ext with an optional '.' followed by an ' ' space or a 'x'
# (\d{2,5}))                    # extension number-part (optional), it might be 2 up to 5 digits
''', re.VERBOSE)

# re.compile(r'((\d\d\d) | (\(\d\d\d\)))?(\s|-)\d\d\d-\d\d\d\d(((ext(\.)?\s)|x)(\d{2,5}))')

# * Create a regex for email addresses

emailRegex = re.compile(r'''

[a-zA-Z0-9_.+]+   # name part, the + stands for: all this characters might appear once or more
@                 # @ symbol
[a-zA-Z0-9_.+]+   # domain name part 

''', re.VERBOSE)

# * Get the text off the clipboard 

text = pyperclip.paste() 

# * Extract the email/phone from this text

extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

print(extractedPhone)
print(extractedEmail)

# todo: copy the extracted email/phone to the clipboard


