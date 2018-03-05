while True:
    input_string = input()
    if input_string == "end":
        break
    str_len = len(input_string)
    middle_index = str_len // 2
    if str_len % 2 == 0:
        first_part = input_string[:middle_index]
        second_part = input_string[middle_index:]
        if first_part == second_part:
            continue
    else:
        first_part = input_string[:middle_index]
        second_part = input_string[middle_index + 1:]
    part_len = len(first_part)
    while part_len != 0:
        if first_part == second_part:
            break
        else:
            first_part = first_part[:-1]
            second_part = second_part[1:]
        part_len = len(first_part)
    middle_part = input_string[part_len:-part_len]
    if part_len != 0:
        replaced_string = middle_part + first_part + middle_part
        print(replaced_string)
    else:
        continue
