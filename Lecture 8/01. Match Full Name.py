import re

input_data = input()
regex = re.compile(r'\b[A-Z][a-z]+ [A-Z][a-z]+\b')
match = regex.findall(input_data)
print(*match,sep=' ')
