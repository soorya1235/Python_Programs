import re
pattern = re.compile("TP")
abc=pattern.findall("This is the TP of the Country TP")
print(abc)
