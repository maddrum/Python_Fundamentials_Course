import os


class IOManager:
    def __init__(self):
        self.file_path = "./Output/06. User Database/users.txt"
        self.passwords = {}

    def reader(self):
        if not os.path.isfile(self.file_path):
            return
        with open(self.file_path) as input_file:
            for item in input_file:
                username = item.split()
                username[1] = username[1].split("\n")[0]
                self.passwords[username[0]] = username[1]

    def writer(self):
        with open(self.file_path, 'w') as user_file:
            for item in self.passwords:
                output_string = item + " " + self.passwords[item] + "\n"
                user_file.write(output_string)


class userDatabase(IOManager):
    def __init__(self):
        IOManager.__init__(self)
        self.user = ''
        self.password = ''
        self.logged_users = []
        self.last_logged_in_user = ''
        self.reader()

    def create_user(self, user, password):
        if user in self.passwords:
            print("The given username already exists.")
        else:
            self.passwords[user] = password

    def login_user(self, user, password):
        if user not in self.passwords:
            print("There is no user with the given username.")
            return
        elif user in self.logged_users:
            print("There is already a logged in user.")
            return
        elif self.passwords[user] != password:
            print("The password you entered is incorrect.")
            return
        else:
            self.logged_users.append(user)

    def logout(self):
        try:
            self.logged_users.pop()
        except IndexError:
            print("There is no currently logged in user.")
        return


database = userDatabase()
while True:
    input_string = input().split()
    if input_string[0] == "exit":
        database.writer()
        break
    elif input_string[0] == "register":
        if input_string[2] != input_string[3]:
            print("The two passwords must match.")
            continue
        database.create_user(user=input_string[1], password=input_string[2])
    elif input_string[0] == "login":
        database.login_user(input_string[1], input_string[2])
    elif input_string[0] == "logout":
        database.logout()
