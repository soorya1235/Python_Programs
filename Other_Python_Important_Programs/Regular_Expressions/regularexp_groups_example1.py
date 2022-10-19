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

pattern1 = re.compile(r'(Mr|Ms|Mrs)\.?\s\w*')
matches = pattern1.finditer(text_to_search)

for match in matches:
    print(match)


