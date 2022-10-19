import re

sentence = 'Start a sentence and Start then bring it to an end'

pattern = re.compile(r'start',re.IGNORECASE)

matches = pattern.search(sentence)
print(matches)
print(matches.group())

print(matches.span())
print(type(matches.span()))