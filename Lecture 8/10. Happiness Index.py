import re

input_data = input()
happy_pattern = r'[:;\(\*c\[][\)D\*\]\}:;]'
sad_pattern = r'[:;\)D\]][\(c\[\{:;]'
happy_regex = re.compile(happy_pattern)
sad_regex = re.compile(sad_pattern)
happy_count_raw = happy_regex.findall(input_data)
sad_count_raw = sad_regex.findall(input_data)
happy_emoticons = [item for item in happy_count_raw if len(list(set(item))) > 1]
sad_emoticons = [item for item in sad_count_raw if len(list(set(item))) > 1]
happy_index = len(happy_emoticons) / len(sad_emoticons)
if happy_index >= 2:
    print(f'Happiness index: {happy_index:.2f} :D')
elif happy_index > 1:
    print(f'Happiness index: {happy_index:.2f} :)')
elif happy_index == 1:
    print(f'Happiness index: {happy_index:.2f} :|')
else:
    print(f'Happiness index: {happy_index:.2f} :(')
print(f'[Happy count: {len(happy_emoticons)}, Sad count: {len(sad_emoticons)}]')
