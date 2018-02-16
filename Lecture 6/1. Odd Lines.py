input_file_path = "./Resources/01. Odd Lines/Input.txt"
output_file_path = "./Output/01. Odd Lines/Output.txt"
with open(input_file_path) as opened_file:
    contents = [item.split("\n")[0] for number, item in enumerate(opened_file) if number % 2 == 1]
    with open(output_file_path, 'w') as output_file:
        for item in contents[:-1]:
            line_to_write = item + "\n"
            output_file.write(line_to_write)
        line_to_write = contents[-1]
        output_file.write(line_to_write)
