import re

pattern = r'\">'
while True:
    input_data = input()
    if input_data == "end":
        break
    input_data = input_data.replace("</a>", "[/URL]")
    input_data = input_data.replace("<a", "[URL")
    regex = re.split(pattern, input_data)
    for index in range(len(regex) - 1):
        regex[index] = regex[index] + '"]'
    output_string = "".join(regex)
    print(output_string)
