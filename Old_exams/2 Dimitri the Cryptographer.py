arr=[0]
read = {}
checker = 0
first = {}
second = {}
third = {}
while checker!=1:
    arr = [i for i in input().strip().split(" -> ")]
    if arr[0] not in ["STOP","END","HALT"]:
        read.update({arr[0]:arr[1]})
    elif arr[0]=="STOP":
        first = dict(read)
        read = {}
    elif arr[0]=="HALT":
        second = dict(read)
        read = {}
    elif arr[0]=="END":
        third = dict(read)
        read = {}
    if first and second and third:
        checker = 1
codIn = input().strip()
codOut = ''
for i in range(0,len(codIn)):
    multiplier = i//6
    if i == 0 or i%6==0:
        a = third.get(second.get(first.get(codIn[i])))
        codOut+=str(a)
    else:
        j = i-multiplier*6
        if j in [1,3,5]:
            a = first.get(codIn[i])
            codOut += str(a)
        else:
            a = second.get(first.get(codIn[i]))
            codOut += str(a)
print(codOut)
