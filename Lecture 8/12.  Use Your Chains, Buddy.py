import re


def modify_string(string_to_modify):
    result = string_to_modify
    pattern_space = r'\s\s+'
    regex_space = re.compile(pattern_space)
    spacer = regex_space.finditer(string_to_modify)
    spaces_counter = []
    for spaces in spacer:
        spaces_counter.append(spaces.group(0))
    spaces_counter = set(spaces_counter)
    for item_local in sorted(spaces_counter, reverse=True):
        result = result.replace(item_local, " ")
    return result


decrypt_dict = {}
for i in range(109, 123):
    item = chr(i - 13)
    decrypt_dict[chr(i)] = item
for i in range(97, 110):
    item = chr(i + 13)
    decrypt_dict[chr(i)] = item
for i in range(0, 10):
    decrypt_dict[i] = i
input_data = input()
pattern = r'<p>(?P<content>.+?)<\/p>*'
regex = re.compile(pattern)
tags = regex.finditer(input_data)
raw_extracted_data = [tag.group('content') for tag in tags]
extracted_data = []
for item in raw_extracted_data:
    modified_item = ''
    for symbol in item:
        if symbol in decrypt_dict:
            modified_item += decrypt_dict[symbol]
        else:
            modified_item += " "
    extracted_data.append(modified_item)
result_str = ''.join(extracted_data)
result_str = modify_string(result_str)
print(result_str)
