import os


class IOManager:
    def __init__(self):
        self.file_path = "./Output/09. Products/stock.txt"
        self.stock = dict()
        self.stock['Food'] = {}
        self.stock['Electronics'] = {}
        self.stock['Domestics'] = {}

    def reader(self):
        if not os.path.isfile(self.file_path):
            return
        with open(self.file_path) as input_file:
            for item in input_file:
                stock_line = item.split()
                stock_line[3] = stock_line[3].split("\n")[0]
                temp_products = [float(stock_line[2]), int(stock_line[3])]
                product = self.stock[stock_line[0]]
                product[stock_line[1]] = temp_products
                self.stock[stock_line[0]] = product

    def stocker(self):
        with open(self.file_path, 'w') as user_file:
            for item in self.stock:
                if self.stock[item]:
                    for product in self.stock[item]:
                        output_string = item + " " + product + " " + " ".join(
                            map(str, self.stock[item][product])) + "\n"
                        user_file.write(output_string)


class products(IOManager):
    def __init__(self):
        IOManager.__init__(self)
        self.reader()

    def stocks_input(self, name, product_type, price, quantity):
        if self.stock[product_type]:
            products_temp = self.stock[product_type]
        else:
            products_temp = {}
        products_temp[name] = [float(price), int(quantity)]
        self.stock[product_type] = products_temp

    def analyze(self):
        for item in sorted(self.stock):
            if self.stock[item]:
                for product in sorted(self.stock[item]):
                    print(f'{item}, Product: {product}')
                    print(f'Price: ${self.stock[item][product][0]:.2f}, Amount Left: {self.stock[item][product][1]}')
            else:
                print("No products stocked")

    def sales(self):
        sales_report = {}
        for item in self.stock:
            type_sum = 0
            if self.stock[item]:
                for product in self.stock[item]:
                    type_sum += self.stock[item][product][0] * self.stock[item][product][1]
                sales_report[item] = type_sum
            else:
                continue
        for item in sorted(sales_report, key=sales_report.get, reverse=True):
            print(f'{item}: ${sales_report[item]}')


database = products()
while True:
    input_str = input().split()
    if input_str[0] == "exit":
        break
    elif input_str[0] == "analyze":
        database.analyze()
    elif input_str[0] == "sales":
        database.sales()
    elif input_str[0] == "stock":
        database.stocker()
    else:
        database.stocks_input(name=input_str[0], product_type=input_str[1], price=input_str[2], quantity=input_str[3])
