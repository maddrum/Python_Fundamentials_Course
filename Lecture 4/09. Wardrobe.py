n = int(input())
wardrobe = {}
printed = []
for i in range(n):
    array = [item for item in input().split(" -> ")]
    inputArray = array[1].split(",")
    if array[0] in wardrobe:
        tempArr = wardrobe[array[0]]
        tempArr += inputArray
        wardrobe[array[0]] = tempArr
    else:
        wardrobe[array[0]] = inputArray
array = [item for item in input().split()]
for item in wardrobe:
    print(f'{item} clothes:')
    result = wardrobe[item]
    for j in result:
        if j in printed:
            continue
        count = result.count(j)
        print(f'* {j} - {count}', end="")
        if item == array[0] and j == array[1]:
            print(" (found!)", end="")
        print()
        printed.append(j)
