import re


def modify_key_or_value(string_to_modify):
    pattern = r'([^ ])+(\s)?'
    regex = re.compile(pattern)
    words = regex.finditer(string_to_modify)
    modified_string = ''
    for word in words:
        modified_string += word.group(0)
    return modified_string


while True:
    data_dict = {}
    input_data = input()
    if input_data == 'END':
        break
    input_data = input_data.replace('%20', ' ')
    input_data = input_data.replace('+', ' ')
    split_check = input_data.split('?')
    if len(split_check) > 1:
        input_data = split_check[1]
    list_of_strings = input_data.split("&")
    for item in list_of_strings:
        item_splitter = item.split('=')
        item_splitter = [item.strip() for item in item_splitter]
        temp_arr = []
        key = modify_key_or_value(item_splitter[0])
        value = modify_key_or_value(item_splitter[1])
        if key in data_dict:
            temp_arr = data_dict[key]
        temp_arr.append(value)
        data_dict[key] = temp_arr
    for item in data_dict:
        print(f'{item}=[', end="")
        print(*data_dict[item], sep=", ", end="")
        print("]", end="")
    print()
