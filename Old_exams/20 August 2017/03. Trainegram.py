import re

pattern = r'(<\[[^a-zA-Z\d]*\]+\.)(\.\[[\da-zA-Z]*\]\.)*'
regex = re.compile(pattern)
found_trains = []
while True:
    input_data = input()
    if input_data == "Traincode!":
        break
    found_train = regex.match(input_data)
    if found_train is None:
        continue
    found_train = found_train.group(0)
    if found_train != input_data:
        continue
    found_trains.append(found_train)
for item in found_trains:
    print(item)
