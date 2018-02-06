arr = list(input())
countArr = [item for item in arr if arr.count(item) > 1]
countArr = [item for item in set(countArr)]
print(countArr)
counter = 0
checker = 0
j = 0
while checker == 0:
    a = len(arr)
    modified = list(arr)
    startCounter = counter
    for i in range(len(arr) - 2):
        if arr[i] not in countArr:
            continue
        if arr[i] == arr[i + 1]:
            modified.pop(i)
            modified.pop(i)
            counter += 1
            break
    arr = list(modified)
    if arr and len(arr) > 1:
        if len(arr) > 2:
            if arr[-1] == arr[-2]:
                counter += 1
                arr.pop()
                arr.pop()
        elif arr[0] == arr[1]:
            counter += 1
            arr.pop()
            arr.pop()
    if startCounter == counter:
        checker = 1
    j += 1
    if j == a:
        break
if len(arr) != 0:
    print(*arr, sep="")
else:
    print("Empty String")
print(f'{counter} operations')
