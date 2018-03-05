import re

pattern = r'(?P<tail>>+)?<(?P<body>\(+)(?P<status>[-\'x])>'
regex = re.compile(pattern)
input_data = input()
checker = regex.findall(input_data)
if not checker:
    print("No fish found.")
    exit()
fishes = regex.finditer(input_data)
counter = 1
for fish in fishes:
    fish_view = fish.group(0)
    tail = fish.group('tail')
    body = fish.group('body')
    status = fish.group('status')
    if tail:
        tail_len = len(tail)
    else:
        tail_len = 0
    body_len = len(body)
    if tail_len == 0:
        tail_type = "None"
    elif tail_len == 1:
        tail_type = "Short"
    elif tail_len in range(2, 6):
        tail_type = "Medium"
    else:
        tail_type = "Long"
    if body_len > 10:
        body_type = "Long"
    elif body_len > 5:
        body_type = "Medium"
    else:
        body_type = "Short"
    if status == "x":
        status_type = "Dead"
    elif status == "'":
        status_type = "Awake"
    else:
        status_type = "Asleep"
    print(f'Fish {counter}: {fish_view}')
    if tail_len != 0:
        print(f'  Tail type: {tail_type} ({tail_len*2} cm)')
    else:
        print(f'  Tail type: {tail_type}')
    print(f'  Body type: {body_type} ({body_len*2} cm)')
    print(f'  Status: {status_type}')
    counter += 1
