input_file1_path = "./Resources/03. Merge Files/FileOne.txt"
input_file2_path = "./Resources/03. Merge Files/FileTwo.txt"
output_file_path = "./Output/03. Merge Files/Output.txt"

with open(input_file1_path) as file1:
    with open(input_file2_path) as file2:
        file1_line = 0
        file2_line = 0
        contents = []
        while file1_line != "" or file2_line != "":
            file1_line = file1.readline().split("\n")[0]
            file2_line = file2.readline().split("\n")[0]
            if file1_line != "":
                contents.append(file1_line)
            if file2_line != "":
                contents.append(file2_line)
        with open(output_file_path, 'w') as output_file:
            writer = [output_file.write((str(item) + "\n")) for item in contents[:-1]]
            output_file.write(contents[-1])
