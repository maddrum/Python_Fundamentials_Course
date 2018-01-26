array = input().split(" ")
n = int(input())
arrayInt = [str(int(i) * n) for i in array]
print(' '.join(arrayInt))
