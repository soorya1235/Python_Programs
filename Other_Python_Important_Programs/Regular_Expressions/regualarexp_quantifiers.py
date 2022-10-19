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



pattern1 = re.compile(r'Mr\.')
pattern2 = re.compile(r'Mr\.?')
pattern3 = re.compile(r'Mr\.?\s[A-Z]+')
pattern4 = re.compile(r'Mr\.?\s\w+')
pattern5 = re.compile(r'Mr\.?\s\w*')

matches1 = pattern1.finditer(text_to_search)
matches2 = pattern2.finditer(text_to_search)
matches3 = pattern5.finditer(text_to_search)


for match in matches3:
    print(match)


