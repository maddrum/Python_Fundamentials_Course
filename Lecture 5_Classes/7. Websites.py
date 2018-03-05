class Website:
    def __init__(self, host, domain, query):
        self.host = host
        self.domain = domain
        self.query = query.split(",")

    def output(self):
        querry_string = ''
        if len(self.query) > 1:
            for item in self.query[:-1]:
                querry_string += "[" + item + "]&"
            querry_string += "[" + self.query[-1] + "]"
            result = f'https://www.{self.host}.{self.domain}/query?={querry_string}'
        else:
            result = f'https://www.{self.host}.{self.domain}'
        return result


collection = []
while True:
    input_data = [item for item in input().split(" | ")]
    if input_data[0] == "end":
        break
    try:
        collection.append(Website(input_data[0], input_data[1], input_data[2]))
    except:
        collection.append(Website(input_data[0], input_data[1], ''))
for item in collection:
    print(item.output())
