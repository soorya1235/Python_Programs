import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
abc abc abc
'''

sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'abc')

matches = pattern.finditer(text_to_search)

#print(list(matches))

print("Matches are")
for match in matches:
    print(match)

#we can slice the stirng uisng span to get the match details

print(text_to_search[1:4])
print(text_to_search[266:269])
print(text_to_search[270:273])
print(text_to_search[274:277])
