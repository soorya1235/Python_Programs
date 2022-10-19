import re

s = 'Python Python is awesome'

new_s = re.sub(r'(\w+)\s+\1', r'\1', s)

print(new_s)