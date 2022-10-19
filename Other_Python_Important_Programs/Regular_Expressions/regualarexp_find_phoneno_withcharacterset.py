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

# pattern = re.compile(r'.')
#
# matches = pattern.finditer(text_to_search)
#
# #print(list(matches))
#
# print("Matches are")
# for match in matches:
#     print(match)
#

#if we need to match only dot...so use \
#below pattern will match any charcter after 3 digit which can be "-" or any character
pattern1 = re.compile(r'\d{1,3}[-.]\d{1,3}[.-]\d{1,4}')

#if i want to find specif to "-" use ths
pattern2 = re.compile(r'\d{1,3}-\d{1,3}-\d{1,4}')

matches1 = pattern1.finditer(text_to_search)
matches2 = pattern2.finditer(text_to_search)

#print(list(matches))

print("Matches are")
for match in matches1:
    print(match)
print("***********************************")
for match in matches2:
    print(match)
