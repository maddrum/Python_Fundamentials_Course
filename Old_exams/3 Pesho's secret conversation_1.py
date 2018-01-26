line1 = input()
line2 = input()
strIn = ''
arrPenka = []
counter = 0
for i in line1:
    if i.isdigit():
        break
c = line1.find(i)
keyPenka = {i:line1[i] for i in range(0,c)}
penka = line1[c:]
for i in range(0,len(penka)-1,2):
    a = penka[i:i+2]
    arrPenka.append(int(a))
for i in line2:
    a = ord(i)
    if a in range(65,91) or a in range(97,123):
        strIn +=i
pesho=strIn[52:]
keyPesho = {i:strIn[i] for i in range(0, 52)}
encryptedPesho =''
for i in pesho:
    a = ord(i)
    if a in range(97,123):
        index = a - 97
    else:
        index = a - 39
    encryptedPesho += keyPesho.get(index)
encryptedPeshoInt = ''
for i in encryptedPesho:
    a = ord(i)
    if a in range(97,123):
        index = a - 97
    else:
        index = a - 39
    if index in range(0,10):
        encryptedPeshoInt += "0"+str(index)
    else:
        encryptedPeshoInt += str(index)
decrKey= {keyPenka.get(i):i for i in range(0,52)}
messagePenka=''
for i in arrPenka:
    if i < 26:
        k = i+97
    else:
        k = i + 39
    letter = chr(k)
    index = int(decrKey.get(letter))
    if index < 26:
        letter = index + 97
    else:
        letter = index + 39
    messagePenka+=chr(letter)
print(messagePenka)
#print Encrypted Pesho - ouput line 2
for i in range(0,52):
    print(keyPesho.get(i),end="")
print(encryptedPeshoInt)








