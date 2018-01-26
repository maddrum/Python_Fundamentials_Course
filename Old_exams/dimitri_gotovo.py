table1 = {}
table2 = {}
table3 = {}

temporaryTable = {}
stopsCount = 0
while stopsCount < 3:
    line = input()

    if line == 'STOP':
        table1 = temporaryTable
        temporaryTable = {}
        stopsCount += 1
        continue
    elif line == 'HALT':
        table2 = temporaryTable
        temporaryTable = {}
        stopsCount += 1
        continue
    elif line == 'END':
        table3 = temporaryTable
        temporaryTable = {}
        stopsCount += 1
        continue

    tokens = line.split(' -> ')
    firstSymbol = tokens[0]
    secondSymbol = tokens[1]

    temporaryTable[firstSymbol] = secondSymbol

encryptedString = input()


def decrypt_string(encrypted_string):
    encrypted_string = list(encrypted_string)

    def replace_chars(encrypted_list, replacementTable, step):
        for i in range(0, len(encrypted_string), step):
            if encrypted_string[i] in replacementTable:
                encrypted_list[i] = replacementTable[encrypted_list[i]]

    replace_chars(encrypted_string, table1, 1)
    replace_chars(encrypted_string, table2, 2)
    replace_chars(encrypted_string, table3, 3)

    return ''.join(encrypted_string)


decryptedString = decrypt_string(encryptedString)

print(decryptedString)
