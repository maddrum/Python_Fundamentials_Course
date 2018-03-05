import re

input_data = input()
pattern = r'\b(?P<day>\d{2})([-./])(?P<month>[A-Z]\w{2})\2(?P<year>\d{4})\b'
regex = re.compile(pattern)
date_match = regex.finditer(input_data)
for match in date_match:
    day = match.group('day')
    month = match.group('month')
    year = match.group('year')
    print(f'Day: {day}, Month: {month}, Year: {year}')
