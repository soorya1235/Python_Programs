import re

email = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

pattern1 = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.com')
pattern2 = re.compile(r'[a-zA-Z.]+@[a-zA-Z]+\.(edu|com)')
#pattern3 = re.compile(r'[a-zA-Z.-]+@[a-zA-Z]+\.(edu|com|net)')
pattern3 = re.compile(r'[a-zA-Z.0-9-]+@[a-zA-Z-]+\.(edu|com|net)')

#commonly used regular expression
pattern4 = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

matches = pattern4.finditer(email)

if matches is not None:
    for match in matches:
        print(match)
        #print(match.group())

