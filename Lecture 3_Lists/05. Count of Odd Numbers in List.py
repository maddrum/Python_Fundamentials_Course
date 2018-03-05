array = input().split()
oddNumbers = [i for i in array if int(i) % 2 != 0]
print(len(oddNumbers))
