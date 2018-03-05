from sys import maxsize

str_len = -maxsize
data = {}
while True:
    input_string = input()
    if input_string == "end":
        break
    letter = input_string.split(":")[0]
    index_array = list(map(int, input_string.split(":")[1].split("/")))
    max_array_member = max(index_array)
    if max_array_member > str_len:
        str_len = max_array_member
    data[letter] = index_array
output_string_list = [" " for i in range(str_len + 1)]
for letter in data:
    for index in data[letter]:
        output_string_list[index] = letter
print(*output_string_list, sep="")
