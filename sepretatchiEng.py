import re

path = 'wordlist.txt'
file = open(path, "r")
result = re.match(r"([\u4e00-\u9fa5]*)([A-Za-z\s]*)", file)
print(result.group(1)) 
print(result.group(2)) 