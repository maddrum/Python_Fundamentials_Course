import re

input_data = input()
pattern = r'(^|(?<=\s))\-?\d+(\.?\d+)?($|(?=\s))'
regex = re.compile(pattern)
matches = regex.finditer(input_data)
for match in matches:
    print(match.group(0), end=" ")
