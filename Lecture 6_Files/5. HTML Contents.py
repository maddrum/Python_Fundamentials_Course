import os


class htmlGenerator:
    def __init__(self):
        self.title = []
        self.body = ["<body>"]

    def title_maker(self, content):
        self.title = ["<!DOCTYPE html>", "<html>", "<head>", "   <title>" + content + "</title>", "</head>"]

    def body_shape(self, tag, content):
        tag_string = f'   <{tag}>'
        close_tag_string = f'</{tag}>'
        whole_line = tag_string + content + close_tag_string
        self.body.append(whole_line)

    def body_end(self):
        self.body.append("</body>")
        self.body.append("</html>")

    def writer(self):
        output_file_path = "./Output/05. HTML Contents/index.html"
        if os.path.isfile(output_file_path):
            os.remove(output_file_path)
        with open(output_file_path, 'a') as html_file:
            for item in self.title:
                formated_string = item + "\n"
                html_file.write(formated_string)
            for item in self.body:
                formated_string = item + "\n"
                html_file.write(formated_string)


html_gen = htmlGenerator()
while True:
    input_string = input().split()
    if input_string[0] == 'exit':
        html_gen.body_end()
        break
    elif input_string[0] == 'title':
        html_gen.title_maker(input_string[1])
    else:
        html_gen.body_shape(input_string[0], input_string[1])

html_gen.writer()
