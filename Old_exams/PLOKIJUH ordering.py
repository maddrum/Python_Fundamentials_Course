def addNew(name):
    global price, contents, checker
    if price.get(name):
        print("STUPIDO!!1")
        return
    else:
        checker = 1
        price.update({name: float(0)})
        contents.update({name: []})
    return


def GEPRISEN(name, price1):
    global price
    price.update({name: float(price1)})
    return


def KOMPONENTUNG(name, component):
    global contents
    tempArr = []
    if component == "SAHRA" or component == "BINGIL" or component == "AMZGA":
        tempArr = contents[name]
        tempArr.append(component)
        contents[name] = tempArr
    else:
        print("BLAH!")
    return


def DECOMPING(name, component):
    global contents
    tempArr = []
    if component == "SAHRA" or component == "BINGIL" or component == "AMZGA":
        tempArr = contents[name]
        try:
            tempArr.index(component)
        except:
            print("YACK!")
            return
        tempArr.remove(component)
        contents[name] = tempArr
    else:
        print("YACK!")
    return


def BLUSS(name1, name2):
    global price
    global contents
    meanPrice = (float(price.get(name1)) + price.get(name2)) / 2
    n1 = len(name1) // 2
    n2 = len(name2) // 2
    newName = name1[:n1] + name2[n2:]
    arrN1 = contents[name1]
    arrN2 = contents[name2]
    for i in arrN2:
        arrN1.append(i)
    if name1 == name2:
        contents.pop(name1)
        price.pop(name1)
    else:
        contents.pop(name1)
        price.pop(name1)
        contents.pop(name2)
        price.pop(name2)
    price.update({newName: float(meanPrice)})
    contents.update({newName: arrN1})


def TULOSTASE():
    global contents
    global price
    global checker
    if checker == 0:
        print("INTEPLOKIJUHAR:(")
        return
    dictPrice = {price[i]: [] for i in price}
    dictContentLen = {i: len(contents[i]) for i in contents}
    for i in dictPrice:
        equal = []
        for j in price:
            if i == price[j]:
                equal.append(j)
                dictPrice.update({price[j]: equal})
    for i in dictPrice:
        tempArr = dictPrice[i]
        ll = len(tempArr)
        if ll == 1:
            continue
        else:
            tempArrSort = list(tempArr)
            for x in tempArr:
                for y in tempArr:
                    if dictContentLen[y] < dictContentLen[x]:
                        tempArrSort[tempArrSort.index(x)], tempArrSort[tempArrSort.index(y)] = tempArrSort[
                                                                                                   tempArrSort.index(
                                                                                                       y)], tempArrSort[
                                                                                                   tempArrSort.index(x)]
            dictPrice.update({i: tempArrSort})
    # try:
    #     tempArr = dictPrice[0]
    #     tempArr.sort()
    #     dictPrice.update({0:tempArr})
    # except KeyError:
    #     pass
    for i in sorted(dictPrice):
        for j in dictPrice[i]:
            print("$$# PLOKIJUH: {}".format(j))
            print("$#$ Price: {0:.1f}".format(price.get(j)))
            print("#$$ Components: ", end="")
            if len(contents[j]) > 1:
                for y in contents[j][:-1]:
                    print(y, end=", ")
                print(contents[j][-1], end="")
            else:
                for h in contents.get(j):
                    print(h, end="")
            print()
    return


arr = ["go"]
price = {}
contents = {}
checker = 0
while arr[0] != 'STOPAAJUHIT!':
    arr = [arr_temp for arr_temp in input().strip().split(' ')]
    if arr[0] == 'NEW':
        addNew(arr[1])
    elif arr[0] == 'GEPRISEN':
        GEPRISEN(arr[1], arr[2])
    elif arr[0] == "KOMPONENTUNG":
        KOMPONENTUNG(arr[1], arr[2])
    elif arr[0] == "DECOMPING":
        DECOMPING(arr[1], arr[2])
    elif arr[0] == "BLUSS":
        BLUSS(arr[1], arr[2])
    elif arr[0] == "TULOSTASE":
        TULOSTASE()
