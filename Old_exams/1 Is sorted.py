array = input().split()
for i in array:
    try:
        i = int(i)
    except:
        print("INVALID INPUT")
        quit()
array = [int(item) for item in array]
for i in range(1, len(array)):
    if array[i] < array[i - 1]:
        print(i)
        quit()
print("SORTED")
