#!/usr/bin/python3
import re 

message = 'My phone number is 415-555-4242 and 415-333-3344'

                              # group 1  group 2  group 3
phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
matchObject = phoneNumberRegex.search(message)

print(matchObject.group())  # print the full group 
print(matchObject.group(1))  # print only the group 1



message2 = 'Batmobile lost a wheel'

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
matchObject = batRegex.search(message2)
print(matchObject.group())  # this prints the output of the method search()