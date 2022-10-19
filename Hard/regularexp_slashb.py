import re

target_str = "Jessa salary is 8000$ She is Python developer"

# \b to word boundary
# \w{6} to match six-letter word
result = re.findall(r"\b\w{5,6}\b", target_str)
print(result)
# Output ['salary', 'Python']

# \b need separate word not part of a word
result = re.findall(r"\bthon\b", target_str)
print(result)
# Output []
