import re

pattern = r'^(/|\\)([a-zA-Z\d]+)(\2)([a-zA-Z\d]+)(\4)(\2)(\4)(\1)$'
regex = re.compile(pattern)
while True:
    input_data = input()
    alphanumeric = ''
    if input_data == "/end/":
        break
    for item in input_data:
        if item.isdigit() or item.isalpha():
            alphanumeric += item
    trimmed_string = input_data[0] + alphanumeric + input_data[-1]
    delta = len(input_data) - len(trimmed_string)
    match = regex.match(trimmed_string)
    if match is None:
        continue
    username_encoded = match.group(2)
    password_encoded = match.group(4)
    username = ''
    password = ''
    for item in username_encoded:
        letter = chr(ord(item) - delta)
        username += letter
    for item in password_encoded:
        letter = chr(ord(item) - delta)
        password += letter
    print(f'user: {username}, pass: {password}')
