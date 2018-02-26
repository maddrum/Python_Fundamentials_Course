N = int(input())
fibb = [1, 1]
counter = 1
for i in range(2, N):
    if i % 2 == 0:
        new_value = fibb[i - 1] + fibb[i - 2]
        counter += 1
        fibb.append(new_value)
    else:
        new_value = counter * fibb[i - 1]
        fibb.append(new_value)
print(fibb[-1])
