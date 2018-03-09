import datetime

date = datetime.date
time = datetime.time
date_format = '%d.%m.%Y'
time_format = '%H:%M:%S'
date_and_time = date_format + "@" + time_format
date_input = datetime.datetime.strptime(input(), date_format)
time_input = datetime.datetime.strptime(input(), time_format)
date_and_time_input = datetime.datetime.strptime(input(), date_and_time)
delta_date = datetime.timedelta(days=5)
delta_time = datetime.timedelta(days=2, minutes=24)
result_date = date_input + delta_date
result_time = time_input + delta_time
result1 = date_input + delta_time
result2 = date_and_time_input + delta_time
print(result_time)
print(result2.strftime(date_and_time))
print(result2)
