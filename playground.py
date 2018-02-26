lst = [1,2,4,5]
check = [2,4]
b= list(filter(lambda x: x if x in check else 0, lst))
print(b)