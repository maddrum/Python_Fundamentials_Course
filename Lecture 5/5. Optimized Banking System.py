import operator


class BankAccount:
    def __init__(self, bank, account, balance):
        self.data = {}
        self.bank = bank
        self.account = account
        self.balance = float(balance)


collection = []
result = {}
while True:
    inputLine = [item for item in input().split(" | ")]
    if inputLine[0] == "end":
        break
    collection.append(BankAccount(inputLine[0], inputLine[1], inputLine[2]))
id = 0
for item in sorted((sorted(collection, key=operator.attrgetter('bank'))), key=operator.attrgetter('balance'),
                   reverse=True):
    print("{0} -> {1:.2f} ({2})".format(item.account, item.balance, item.bank))
