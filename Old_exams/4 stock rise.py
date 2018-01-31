filename = input()
jump = float(input())
try:
    file = open(filename)
except:
    print("INVALID INPUT")
    quit()
rawData = file.readlines()
if len(rawData) == 0:
    print("INVALID INPUT")
    quit()
stocks = {}
for i in rawData:
    temp = i.split(",")
    try:
        temp_price = float(temp[1].split("\\")[0])
    except:
        print("INVALID INPUT")
        quit()
    stocks.update({temp[0]: temp_price})
itemLast = 0
counter = 0
checker = 0
for item in stocks:
    counter += 1
    if itemLast == 0:
        itemLast = item
        continue
    else:
        diff = stocks[item] - stocks[itemLast]
        percent = diff / stocks[itemLast] * 100
        if percent >= jump:
            checker = 1
            print("{0} {1:.2f}".format(item, percent))
        itemLast = item
if checker == 0:
    print(f'NO DRASTIC CHANGES; RECORDS COUNT: {counter}')
