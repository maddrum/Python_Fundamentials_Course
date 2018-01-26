array = input().split()

for i in range(1, len(array), 2):
    if int(array[i]) % 2 != 0:
        print(f'Index {i} -> {array[i]}')
