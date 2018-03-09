import re

pattern = r'^([0-9]+)([A-Za-z]+)([^A-Za-z]+)?$'
regex = re.compile(pattern)
while True:
    input_data = input()
    if input_data == "Over!":
        break
    message_len_input = int(input())
    match = regex.search(input_data)
    if match is None:
        continue
    message = match.group(2)
    indexes_before = list(map(int, list(match.group(1))))
    if match.group(3):
        indexes_after = list(map(int, [item for item in list(match.group(3)) if item.isdigit()]))
    else:
        indexes_after = []
    message_len = len(message)
    if message_len != message_len_input:
        continue
    message_key = ''
    indexes = indexes_before + indexes_after
    for item in indexes:
        if item > message_len - 1:
            temp_sign = " "
        else:
            temp_sign = message[item]
        message_key += temp_sign
    print(f'{message} == {message_key}')
