trainer_dict = {}
courses_dict = {}
servers_minutes = {1: 0}
servers_lectures = {}
current_server = 1
while True:
    input_data = input()
    input_data_check = input_data.split()
    if input_data_check[0] == 'scrape':
        course_or_train = input_data_check[1]
        course_or_trainer_name = input_data_check[2]
        break
    input_data_split = input_data.split(";")
    temp_dict = {item.split(":")[0]: item.split(":")[1] for item in input_data_split}
    trainer = temp_dict['trainer']
    course = temp_dict['course']
    lecture = temp_dict['lecture']
    duration = temp_dict['duration']
    duration_split = duration.split("h")
    duration_split[1] = duration_split[1].replace("m", "")
    hours = int(duration_split[0])
    minutes = int(duration_split[1])
    total_minutes = hours * 60 + minutes
    trainer_input = course + "$$$" + lecture + "$$$" + str(total_minutes)
    course_input = trainer + "$$$" + lecture + "$$$" + str(total_minutes)
    temp_arr = []
    if trainer in trainer_dict:
        temp_arr = trainer_dict[trainer]
    temp_arr.append(trainer_input)
    trainer_dict[trainer] = temp_arr
    temp_arr = []
    if course in courses_dict:
        temp_arr = courses_dict[course]
    temp_arr.append(course_input)
    courses_dict[course] = temp_arr
    current_server_minutes = servers_minutes[current_server]
    total_new_minutes = total_minutes + current_server_minutes
    if total_new_minutes > 600:
        current_server += 1
        total_new_minutes = total_minutes
    servers_minutes[current_server] = total_new_minutes
    key = trainer + "$$$" + course + "$$$" + lecture + "$$$" + str(total_minutes)
    if key in servers_lectures:
        temp_arr = servers_lectures[key]
    else:
        temp_arr = []
    temp_arr.append(current_server)
    servers_lectures[key] = temp_arr
if course_or_train == 'course':
    try:
        output_arr = courses_dict[course_or_trainer_name]
    except KeyError:
        exit()
    total_duration = 0
    for item in output_arr:
        i = 0
        output_arr_split = item.split("$$$")
        trainer = output_arr_split[0]
        lecture = output_arr_split[1]
        duration = int(output_arr_split[2])
        total_duration += duration
        key = trainer + "$$$" + course_or_trainer_name + "$$$" + lecture + "$$$" + str(duration)
        server = servers_lectures[key]
        for single_item in server:
            print(
                f'https://streamcdn{single_item}.softuni.bg/course={course_or_trainer_name}&lecture={lecture}&trainer={trainer}')
            i += 1
else:
    try:
        output_arr = trainer_dict[course_or_trainer_name]
    except KeyError:
        exit()
    total_duration = 0
    for item in output_arr:
        output_arr_split = item.split("$$$")
        course = output_arr_split[0]
        lecture = output_arr_split[1]
        duration = int(output_arr_split[2])
        total_duration += duration
        key = course_or_trainer_name + "$$$" + course + "$$$" + lecture + "$$$" + str(duration)
        server = servers_lectures[key]
        for single_item in server:
            print(
                f'https://streamcdn{single_item}.softuni.bg/course={course}&lecture={lecture}&trainer={course_or_trainer_name}')
hours = total_duration // 60
minutes = total_duration - hours * 60
print(f'total duration: {hours:02}:{minutes:02}:00')
