from math import ceil

budget = float(input())
clients = int(input())
gigabytes = int(input())
hosts = int(input())
uptime = float(input())
servers_needed = ceil(clients / 50)
storage_needed = ceil(gigabytes / 0.5)
hourly = servers_needed * 2 + 0.5 * storage_needed
daily = hourly * 24
hosts_cost = hosts * 10
monthly = daily * 30
total_cost = (monthly + hosts_cost) * uptime / 100
if total_cost <= budget:
    left = budget - total_cost
    print(f'Clouds Ahoy! Monthly cost: ${total_cost:.2f} (${left:.2f} leftover)')
else:
    needed_more = total_cost - budget
    print(f'Stay Grounded! Monthly cost: ${total_cost:.2f} (Need ${needed_more:.2f} more)')
