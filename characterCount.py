# this program will count how many times a character appeared in the message.

import pprint  # ? this will print the dictionaries in a pretty way.

message = 'it was bright cold day in April, and the clcoks were striking thirteen'
count = {}

for character in message.upper():
  count.setdefault(character, 0)  # ? The setdefault method returns the value of the item with the specified key: dictionary.setdefault(keyname, value)
  # count[character] = count[character] + 1
  count[character] += 1

# print(count)
pprint.pprint(count)