import re

input_data = input()
pattern = r'(([2-9]|10)|[JQKA])[SHDC]'
regex = re.compile(pattern)
cards = regex.finditer(input_data)
for card in cards:
    print(card.group(0), end=" ")
