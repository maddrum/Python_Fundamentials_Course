import datetime

time_format = '%H:%M:%S'

time = datetime.time
start_hour = datetime.datetime.strptime(input(), time_format)
steps = int(input())
steps_for_second = int(input())
sum_seconds = steps * steps_for_second
sum_seconds_trim = sum_seconds % 86400
total_seconds = datetime.timedelta(seconds=sum_seconds_trim)
arrival_time = start_hour + total_seconds
print(f'Time Arrival: {arrival_time.strftime(time_format)}')
