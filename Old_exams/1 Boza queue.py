checker = 1
queue = []
while checker != 0:
    arr = [i for i in input().strip().split(" ")]
    if arr[0] == "ADD":
        queue.append(str((arr[1])))
        # print(queue)
    elif arr[0] == "NEXT":
        a = queue.pop(0)
        print(a)
        checker = len(queue)
        # print(queue)
    elif arr[0] == "SKIP":
        queue.pop(0)
        checker = len(queue)
        # print(queue)
    elif arr[0] == "REM":
        for i in range(0,queue.count(arr[1])):
            queue.remove(arr[1])
            checker = len(queue)
        # print(queue)
    elif arr[0] == "CLEANUP":
        ll = [len(i) for i in queue]
        temp = []
        for i in range(0,len(ll)):
            if ll[i]%2 == 0:
               temp.append(queue[i])
        for i in temp:
            print(i)
            queue.remove(i)
        checker = len(queue)
        # print(queue)
    elif arr[0] == "CLEANDOWN":
        temp = []
        ll = [len(i) for i in queue]
        for i in range(0,len(ll)):
            if ll[i]%2==0 and i%2!=0:
                temp.append(queue[i])
        for i in temp:
            queue.remove(i)
        # print(queue)
        checker = len(queue)