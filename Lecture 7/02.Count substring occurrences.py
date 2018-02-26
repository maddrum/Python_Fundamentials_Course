input_string = input()
input_string_lower = input_string.lower()
search_string = input()
search_string_lower = search_string.lower()
counter = 0
index = 0
while True:
    index = input_string_lower.find(search_string_lower, index + 1)
    if index == -1:
        break
    counter += 1
index = input_string_lower.find(search_string_lower)
if index == 0:
    counter += 1
print(counter)
