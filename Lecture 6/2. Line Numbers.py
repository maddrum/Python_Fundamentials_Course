input_file_path = "./Resources/02. Line Numbers/Input.txt"
output_file_path = "./Output/02. Line Numbers/Output.txt"
with open(input_file_path) as input_file:
    contents = [str(number + 1) + ". " + content for number, content in enumerate(input_file)]
    with open(output_file_path, 'w') as output_file:
        writer = [output_file.write(item) for item in contents]
