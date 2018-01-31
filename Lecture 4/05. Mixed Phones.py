phoneBook = {}
while True:
    inputArray = [item for item in input().split(" : ")]
    if inputArray[0] == "Over" and len(inputArray) == 1:
        break
    if inputArray[0].isnumeric():
        phoneBook[inputArray[1]] = inputArray[0]
    else:
        phoneBook[inputArray[0]] = inputArray[1]
for item in sorted(phoneBook):
    print(item, phoneBook[item], sep=' -> ')
