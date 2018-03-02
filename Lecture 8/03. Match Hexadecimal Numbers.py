import re

input_data = input()
pattern = r'\b(?:0x)?[0-9A-F]+\b'
regex = re.compile(pattern)
hexes = regex.finditer(input_data)
for hex in hexes:
    print(hex.group(0), end=" ")
