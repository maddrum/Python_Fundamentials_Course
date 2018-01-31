from math import ceil

shells = {}
while True:
    arr = [item for item in input().split()]
    if arr[0] == 'Aggregate':
        break
    if arr[0] in shells:
        tempArr = [int(item) for item in shells[arr[0]] if item != int(arr[1])]
        tempArr.append(int(arr[1]))
    else:
        tempArr = []
        tempArr.append(int(arr[1]))
    shells[arr[0]] = tempArr
for item in shells:
    print(f'{item} -> ', end="")
    print(*shells[item], sep=", ", end="")
    sumShell = sum(shells[item])
    countShell = len(shells[item])
    average = ceil(sumShell - sumShell / countShell)
    print(f' ({average})')
