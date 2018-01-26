def CERTIFICATE(user,contest):
    global cert
    global rank
    if cert.get(user) != None:
        a = cert[user]
        for i in a:
            if i == contest:
                print("Certificate already exists")
                return
        a.append(str(contest))
        cert.update({user:a})
        return
    else:
        a = [contest]
        cert.update({user:a})
        return
def SOLUTION(user,contest,task,solID,points):
    global solution
    if solution.get(solID) != None:
        print("Solution already exists")
        return
    a = [contest,user,task,float(points)]
    solution.update({solID:a})
    if userSolution.get(user) == None:
        b = [solID]
        userSolution.update({user:b})
    else:
        b = userSolution[user]
        b.append(solID)
        userSolution.update({user:b})
    rankKey = user + "+" +contest
    if rank.get(rankKey)!=None:
        a = float(rank.get(rankKey))
        a+=float(points)
        rank.update({rankKey:float(a)})
    else:
        rank.update({rankKey:points})
    return
def RANKLIST(contest):
    global rank
    output = {}
    total = 0
    counter = 0
    for i in rank:
        j = i.find("+")
        con = i[(j+1):]
        if con == contest:
            a = float(rank.get(i))
            output.update({i[:j]:a})
            total += 1
    for i in sorted(output, key=output.get, reverse = True):
        if counter == total-1:
            print(i)
        else:
            print(str(i)+",",end="")
        counter +=1
    return
def GETSOLUTION(solID):
    global solution
    if solution.get(solID) == None:
        print("Solution not found")
        return
    else:
        output = solution[solID]
        print("User: {}, Contest: {}, Task: {}, Points: {}".format(output[1],output[0],output[2],output[3]))
        return
def GETCERTIFICATE(user,contest):
    global cert
    global solution
    global userSolution
    if cert.get(user) == None:
        print("Certificate not found")
        return
    a = cert.get(user)
    checker = 0
    for i in a:
        if i == contest:
            checker = 1
    if checker == 0:
        print("Certificate not found")
        return
    taskPoints = {}
    b = userSolution[user]
    for i in b:
        a = solution[i]
        if a[0] !=contest:
            continue
        if taskPoints.get(a[2]) == None:
            taskPoints.update({a[2]:float(a[3])})
        elif taskPoints.get(a[2])<a[3]:
            taskPoints.update({a[2]:float(a[3])})
    sumP = 0
    for i in taskPoints:
        sumP+=taskPoints.get(i)
    print(sumP)
    return
def GETCERTIFICATES(user):
    global cert
    if cert.get(user) == None:
        print("Certificate not found")
        return
    a = cert[user]
    a.sort()
    for i in a[:-1]:
        print(i + ",",end="")
    print(a[-1])
    return
cert = {}
solution = {}
rank = {}
userSolution = {}
arr = [0]
while arr[0] != "QUIT":
    arr = [i for i in input().strip().split(' ')]
    if arr[0] == "ADD":
        if arr[1] == "CERTIFICATE":
            CERTIFICATE(arr[2],arr[3])
        if arr[1] == "SOLUTION":
            SOLUTION(arr[2],arr[3],arr[4],arr[5],arr[6])
    if arr[0] == "GET":
        if arr[1] == "RANKLIST":
            RANKLIST(arr[2])
        if arr[1] == "SOLUTION":
            GETSOLUTION(arr[2])
        if arr[1] == "CERTIFICATE":
            GETCERTIFICATE(arr[2],arr[3])
        if arr[1] == "CERTIFICATES":
            GETCERTIFICATES(arr[2])