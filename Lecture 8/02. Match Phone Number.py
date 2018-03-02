import re

input_string = input()
pattern = r'\+359([ -])2\1\d{3}\1\d{4}\b'
regex = re.compile(pattern)
phone_numbers = regex.finditer(input_string)
for phone in phone_numbers:
    print(phone.group(0), end=" ")
