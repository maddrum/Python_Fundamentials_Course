def mover(move, step):
    global currentPosI, currentPosJ, currentPosK, notDead, points, inputArr
    if not notDead:
        return
    if move == 'up':
        for i in range(currentPosI - 1, currentPosI - step - 1, -1):
            try:
                pointsGet = inputArr[i][currentPosJ][currentPosK]
            except:
                pointsGet = 'o'
            if pointsGet == 'a':
                points += 1
                inputArr[i][currentPosJ][currentPosK] = 'o'
        currentPosI -= step
    elif move == 'down':
        for i in range(currentPosI + 1, currentPosI + step + 1):
            try:
                pointsGet = inputArr[i][currentPosJ][currentPosK]
            except:
                pointsGet = 'o'
            if pointsGet == 'a':
                points += 1
                inputArr[i][currentPosJ][currentPosK] = 'o'
        currentPosI += step
    elif move == 'forward':
        for i in range(currentPosJ - 1, currentPosJ - step - 1, -1):
            try:
                pointsGet = inputArr[currentPosI][i][currentPosK]
            except:
                pointsGet = 'o'
            if pointsGet == 'a':
                points += 1
                inputArr[currentPosI][i][currentPosK] = 'o'
        currentPosJ -= step
    elif move == 'backward':
        for i in range(currentPosJ + 1, currentPosJ + step + 1):
            try:
                pointsGet = inputArr[currentPosI][i][currentPosK]
            except:
                pointsGet = 'o'
            if pointsGet == 'a':
                points += 1
                inputArr[currentPosI][i][currentPosK] = 'o'
        currentPosJ += step
    elif move == 'left':
        for i in range(currentPosK - 1, currentPosK - step - 1):
            try:
                pointsGet = inputArr[currentPosI][currentPosJ][i]
            except:
                pointsGet = 'o'
            if pointsGet == 'a':
                points += 1
                inputArr[currentPosI][currentPosJ][i] = 'o'
        currentPosK -= step
    elif move == 'right':
        for i in range(currentPosK + 1, currentPosK + step + 1):
            try:
                pointsGet = inputArr[currentPosI][currentPosJ][i]
            except:
                pointsGet = 'o'
            if pointsGet == 'a':
                points += 1
                inputArr[currentPosI][currentPosJ][i] = 'o'
        currentPosK += step
    return


def deathCheck(i, j, k):
    global notDead
    if not notDead:
        return
    if i < 0 or j < 0 or k < 0:
        notDead = False
    try:
        check = inputArr[i][j][k]
    except IndexError:
        notDead = False
    return


points = 0
notDead = True
currentPosI = 0
currentPosJ = 0
currentPosK = 0
N = int(input())
inputArr = []
for i in range(N):
    tempArr = input().split(" | ")
    inputArr.append(tempArr)
inputArrModified = []
for i in range(N):
    tempArr = []
    for j in range(N):
        tempZ = list(inputArr[j][i])
        for k in tempZ:
            if k == "s":
                currentPosI = i
                currentPosJ = j
                currentPosK = tempZ.index(k)
        tempArr.append(tempZ)
    inputArrModified.append(tempArr)
inputArr = list(inputArrModified)
move = input()
while True:
    inputMove = input().split(' in ')
    lastMove = move
    move = inputMove[0]
    step = int(inputMove[1].split()[0])
    if move == 'end':
        mover(lastMove, step)
        deathCheck(currentPosI, currentPosJ, currentPosK)
        break
    mover(lastMove, step)
    deathCheck(currentPosI, currentPosJ, currentPosK)
print(f'Points collected: {points}')
if not notDead:
    print('The snake dies.')
