import re

allowed_chars = [str(item) for item in range(10)]
allowed_chars.append("<")
allowed_chars.append(">")
diamonds_value = []
pattern = r'<\d+>'
regex = re.compile(pattern)
input_data = input()
filtered_string = "".join(list(filter(lambda x: x in allowed_chars, input_data)))
diamonds = regex.findall(filtered_string)
for diamond in diamonds:
    numbers = map(int, list(diamond[1:-1]))
    sumD = sum(numbers)
    diamonds_value.append(sumD)
if diamonds_value:
    for item in diamonds_value:
        print(f'Found {item} carat diamond')
else:
    print("Better luck next time")
