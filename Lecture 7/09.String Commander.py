class StringManipulator:
    def __init__(self, string_to_manipulate, usr_command, command_parameter1, command_parameter2):
        self._string_to_manipulate = string_to_manipulate
        self._usr_command = usr_command
        self._command_parameter1 = command_parameter1
        self._command_parameter2 = command_parameter2
        if self._usr_command == "Left":
            self.result = self.left()
        elif self._usr_command == "Right":
            self.result = self.right()
        elif self._usr_command == "Insert":
            self.result = self.insert()
        elif self._usr_command == "Delete":
            self.result = self.delete()

    def left(self):
        count_times = int(self._command_parameter1)
        result_string = self._string_to_manipulate
        for i in range(count_times):
            result_string = result_string[1:] + result_string[:1]
        return result_string

    def right(self):
        count_times = int(self._command_parameter1)
        result_string = self._string_to_manipulate
        for i in range(count_times):
            result_string = result_string[-1] + result_string[:-1]
        return result_string

    def insert(self):
        slicer = int(self._command_parameter1)
        str_to_insert = str(self._command_parameter2)
        if slicer != 0:
            result_string = self._string_to_manipulate[:slicer] + str_to_insert + self._string_to_manipulate[
                                                                                  slicer + 1:]
        else:
            result_string = str_to_insert + self._string_to_manipulate
        return result_string

    def delete(self):
        slicer1 = int(self._command_parameter1)
        slicer2 = int(self._command_parameter2) + 1
        result_string = self._string_to_manipulate[:slicer1] + self._string_to_manipulate[slicer2:]
        return result_string


input_string = input()
manipulated_string = input_string

while True:
    user_command = input()
    if user_command == "end":
        break
    user_command = user_command.split()
    if len(user_command) == 2:
        user_command.append('zero_zero')
    result = StringManipulator(string_to_manipulate=manipulated_string, usr_command=user_command[0],
                               command_parameter1=user_command[1], command_parameter2=user_command[2]).result
    manipulated_string = result
print(manipulated_string)
