#!/usr/bin/python3
import re



      # ! Matching 0 or 1 times ?

print('\n\t Match 0 or 1 times ?:')
batRegex = re.compile(r'Bat(wo)?man')  #todo: this is the (wo) group

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



print('\n\t Matches 0 or more times *:')

      # ! Matching 0 or more times *

batRegex = re.compile(r'Bat(wo)*man')
matchObject = batRegex.search('The aventures of Batman')
print(matchObject.group())  # Matches 0 times

matchObject = batRegex.search('The aventures of Batwoman')
print(matchObject.group())  # matches 1 time

matchObject = batRegex.search('The aventures of Batwowowowoman')
print(matchObject.group())  # matches several times.



print('\n\t Matches 1 or more times +:')

      # ! Matching 1 or more times +

batRegex = re.compile(r'Bat(wo)+man')
matchObject = batRegex.search('The aventures of Batman')
print(matchObject)  # None, because it did not match at least 1 time.

matchObject = batRegex.search('The aventures of Batwoman')
print(matchObject.group())  # it did match 1 time

matchObject = batRegex.search('The aventures of Batwowowowoman')
print(matchObject.group())  # it did match more than 1 time.



print('\n\t Matching an specific number of times {x}:')

      # ! Matching an specific number of times {x}

haRegex = re.compile(r'(Ha){3}')  # ? this will match all the patterns HaHaHa
matchObject = haRegex.search('He said "HaHaHa"')
print(matchObject.group())




print('\n\t Matching at least and at most {x,y}:')

      # ! Matching at least and at most {x,y}

haRegex = re.compile(r'(Ha){3,5}')
matchObject = haRegex.search('he said "HaHaHa"')
print(matchObject.group())

matchObject = haRegex.search('he said "HaHaHaHa"')
print(matchObject.group())

matchObject = haRegex.search('he said "HaHaHaHaHa"')
print(matchObject.group())



print('\n\t Greedy and NonGreedy match')

      # ! Greedy and NonGreedy match

digitRegex = re.compile(r'(\d){3,7}')  # ? This is a greedy match, this will match the longest possible result
matchObject = digitRegex.search('1234567890')
print(matchObject.group())  # this will only print 12345

digitRegex = re.compile(r'(\d){3,5}?')  # ? The ? make it a nongreedy match, this will match the shorest possible resutl
matchObject = digitRegex.search('1234567890')
print(matchObject.group())  # this will only print 123