checker = 0
dict = {}

while True:
    inputData = [item for item in input().split(" = ")]
    if inputData[0] == 'end' and len(inputData) == 1:
        break
    try:
        int(inputData[1])
        checker = 1
    except:
        pass
    if checker == 1:
        dict[inputData[0]] = int(inputData[1])
    elif inputData[1] in dict:
        dict[inputData[0]] = dict[inputData[1]]
    checker = 0
for item in dict:
    print(item, dict[item], sep=" === ")
