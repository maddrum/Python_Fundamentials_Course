class Exercise:
    def __init__(self, topic, course_name, link, problems):
        self.topic = topic
        self.course_name = course_name
        self.judge_contest_link = link
        self.problems = problems


collection = []
while True:
    inputLine = [item for item in input().split(" -> ")]
    if inputLine[0] == "go go go":
        break
    collection.append(Exercise(inputLine[0], inputLine[1], inputLine[2], inputLine[3].split(", ")))
for item in collection:
    print(f'Exercises: {item.topic}')
    print(f'Problems for exercises and homework for the "{item.course_name}" course @ SoftUni.')
    print(f'Check your solutions here: {item.judge_contest_link}')
    for i in range(len(item.problems)):
        print("{}. {}".format(i + 1, item.problems[i]))
