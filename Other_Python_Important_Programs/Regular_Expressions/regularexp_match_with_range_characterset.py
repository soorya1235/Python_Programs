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

cat
bat
mat
rat
'''

pattern1 = re.compile(r'[1-5]')
pattern2 = re.compile(r'[a-z]')
pattern3 = re.compile(r'[A-Z]')
pattern3 = re.compile(r'^[A-Z]')  #will match any thing which is not A-Z
pattern4 = re.compile(r'[^b]at')  # will match cat,mat,rat but not bat

mathes = pattern3.finditer(text_to_search)

for match in mathes:
    print(match)
