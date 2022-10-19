import re

#use of finditer which will show the match and span.
str ="aaaaaabeffbhcccaaaaaa"
pattern = re.compile(r'^a{5}')
matches = pattern.finditer(str)
for match in matches:
    print(match)
    print(match.span())



#example 2
pattern = re.compile(r'a{5}')
matches1 = pattern.findall(str)
print(matches1) #print the list

#example3
#to match at the start of the string.
pattern = re.compile(r'^a{6}')
matches2 = pattern.match(str)
print(matches2.group())

print("Below is the example of search")
#example4
#to match at the start of the string.
pattern = re.compile(r'a{6}')
matches3 = pattern.search(str)
print(matches3.group())


print("Below is the example of substitue")
#example4
#to match at the start of the string.
matches4 = re.sub(r'a{6}','soorya',str)
print(matches4) #replaces with soorya in the stirng
print(str)      #print the original stirng

print("Below is the example of substitue with compile.")
#example4
#to match at the start of the string.
pattern = re.compile(r'a{6}')
matches4 = re.sub(pattern,'soorya',str)
print(matches4) #replaces with soorya in the stirng
print(str)      #print the original stirng

#example of spliting a string.
lst = "abc  bbb  ddd"
list_one = re.split(r'\s+',lst)
print(list_one)

#program to search for the digit
target_str = "My roll number is 25"
res = re.findall(r"\d", target_str)
# extract mathing value
print(res) 
# Output [2, 5]


#Program to find the path inside the expresion.
print("without raw string:")
# path_to_search = "c:\example\task\new"
target_string = r"c:\example\task\new\exercises\session1"

# regex pattern
print("without raw string:")
# path_to_search = "c:\example\task\new"
target_string = r"c:\example\task\new\exercises\session1"

# regex pattern
pattern = r"^c:\\example\\task\\new"
# \n and \t has a special meaning in Python
# Python will treat them differently
res = re.search(pattern, target_string)
print(res.group())

#when we run the above program we will get error,because \t and \n has special meaning...
#so we need to replace the pattern = "^c:\\example\\task\\new" with pattern = r"^c:\\example\\task\\new"

import re
#python program to match the \d
result = re.search('\d', '\d')
print(result)
result = re.search(r'\\d','\d')
print(result.group())
#Output
#This gives the output
#None
#\d

#how to match case sensitive in regular exp
str="APPLEisthe coutnry of india"
pattern = re.compile(r'apple',re.I)
matches = pattern.search(str)
print(matches)

#program to display the use of group(1),match(),end(),span using sub
str="apple is the coutnry of is india apple"
match = re.subn(r'is','govinda',str)
print(match)
#print(match.start)


#
import re

string = '39801 356, 2102 1111'

# Three digit number followed by space followed by two digit number
pattern = '(\d{3}) (\d{2})'

# match variable contains a Match object.
match = re.search(pattern, string) 

if match:
  print(match.group())
else:
  print("pattern not found")

print(match.group)  
print(match.group(1))  
print(match.group(2))  
print(match.start())  
print(match.end())
print(match.span())
