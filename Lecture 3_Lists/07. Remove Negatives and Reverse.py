array = input().split()
new_arr = [int(item) for item in array if int(item) > 0][::-1]
if new_arr:
    for i in new_arr:
        print(i, end=" ")
else:
    print("empty")
