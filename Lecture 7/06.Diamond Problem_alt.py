input_string = input()
allowed_chars = [str(item) for item in range(10)]
allowed_chars.append("<")
allowed_chars.append(">")
filtered_string = "".join(list(filter(lambda x: x in allowed_chars, input_string)))
diamonds = []
while True:
    diamond_value = ''
    diamond_value_int = 0
    if not filtered_string:
        break
    if filtered_string[0] == ">":
        filtered_string = filtered_string[1:]
    if filtered_string[-1] == "<":
        filtered_string = filtered_string[:-1]
    if filtered_string[0] != "<":
        temp_finder = filtered_string.find("<")
        if temp_finder == -1:
            break
        filtered_string = filtered_string[temp_finder:]
    while True:
        if len(filtered_string) < 2:
            break
        if filtered_string[0] == "<" and filtered_string[1] == "<":
            filtered_string = filtered_string[1:]
        else:
            break
    while True:
        if len(filtered_string) < 2:
            break
        if filtered_string[-1] == ">" and filtered_string[-2] == ">":
            filtered_string = filtered_string[:-1]
        else:
            break
    current_start_diamond_index = filtered_string.find("<")
    current_end_diamond_index = filtered_string.find(">")
    if current_start_diamond_index == -1 or current_end_diamond_index == -1:
        break
    if current_start_diamond_index < current_end_diamond_index:
        diamond_value = filtered_string[current_start_diamond_index + 1:current_end_diamond_index]
        filtered_string = filtered_string[current_end_diamond_index + 1:]
    for item in diamond_value:
        diamond_value_int += int(item)
    diamonds.append(diamond_value_int)
if diamonds:
    for item in diamonds:
        print(f'Found {item} carat diamond')
else:
    print("Better luck next time")
