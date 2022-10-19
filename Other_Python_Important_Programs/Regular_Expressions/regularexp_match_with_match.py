
import re

sentence = 'Start a sentence and Start then bring it to an end'

pattern = re.compile(r'Start')

#match will match at the beigng of group,else it will fail
matches = pattern.match(sentence)
matches1 = pattern.search(sentence)
matches2 = pattern.findall(sentence)

#search method will search the entimre and give the first match

print(matches.group())
print(matches1.group())
print(matches2)