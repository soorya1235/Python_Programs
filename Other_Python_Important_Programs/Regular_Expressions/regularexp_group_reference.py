import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern1 = re.compile(r'https?://(www.)?(\w+)(\.\w+)')

matches = pattern1.finditer(urls)

# for match in matches:
#     print(match)
#     print(match.group(0))
#     print(match.group(1))
#     print(match.group(2))
#     print(match.group(3))

subbed_url = pattern1.sub(r'\2\3',urls)
print(subbed_url)

