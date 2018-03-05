class User:
    def __init__(self, username, received_messages):
        self.username = username
        self.received_messages = received_messages


class Message:
    def __init__(self, content, sender):
        self.content = content
        self.sender = sender


users = {}
while True:
    input_string = input()
    if input_string == "exit":
        break
    input_string = input_string.split()
    if input_string[0] == "register":
        temp_arr = []
        users.update({input_string[1]: User(input_string[1], temp_arr)})
    elif input_string[0] not in users or input_string[2] not in users:
        continue
    else:
        receiver = input_string[2]
        sender = input_string[0]
        message = input_string[3]
        temp = users[receiver].received_messages
        new_message = Message(content=message, sender=sender)
        temp.append(new_message)
        newUser = User(receiver, temp)
        users.update({receiver: newUser})
input_string = [item for item in input().split()]
user1 = input_string[0]
user2 = input_string[1]
user1_messages = [item.content for item in users[user1].received_messages if item.sender == user2]
user2_messages = [item.content for item in users[user2].received_messages if item.sender == user1]
max_len = max(len(user1_messages), len(user2_messages))
if max_len == 0:
    print("No messages")
    exit()
for i in range(max_len):
    try:
        print(f'{user1}: {user2_messages[i]}')
    except:
        pass
    try:
        print(f'{user1_messages[i]} :{user2}')
    except:
        pass
