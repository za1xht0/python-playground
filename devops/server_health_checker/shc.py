import sys
import psutil

print('Server Health Checker\n')
is_on = int(input('Начинаем?\n1. Да\n2. Нет\n'))
cpu_ram_ok = 80
cpu_ram_warning = 90
disk_ok = 90
disk_warning = 95

def cpu_check(cpu):
    if cpu < cpu_ram_ok:
        return 'OK'
    elif cpu <= cpu_ram_warning:
        return 'WARNING'
    else:
        return 'CRITICAL'

def ram_check(ram):
    if ram < cpu_ram_ok:
        return 'OK'
    elif ram <= cpu_ram_warning:
        return 'WARNING'
    else:
        return 'CRITICAL'

def disk_check(disk):
    if disk < disk_ok:
        return 'OK'
    elif disk <= disk_warning:
        return 'WARNING'
    else:
        return 'CRITICAL'

def service_status(cpu_result, ram_result, disk_result):
    if cpu_result == 'OK' and ram_result == 'OK' and disk_result == 'OK':
        return 'OK'
    elif cpu_result == 'CRITICAL' or ram_result == 'CRITICAL' or disk_result == 'CRITICAL' :
        return 'CRITICAL'
    elif cpu_result == 'WARNING' or ram_result == 'WARNING' or disk_result == 'WARNING' :
        return 'WARNING'
    
def get_exit_code(status):
    if status == 'OK':
        return 0
    elif status == 'WARNING':
        return 1
    elif status == 'CRITICAL':
        return 2

def main(cpu, ram, disk):
    cpu_result = cpu_check(cpu)
    ram_result =  ram_check(ram)
    disk_result =  disk_check(disk)
    serv = service_status(cpu_result, ram_result, disk_result)
    exit_code = get_exit_code(serv)
    return f'\nServer Health Checker\n\nCPU: {cpu}% ---- {cpu_result}\nMemory: {ram}% ---- {ram_result}\nDisk: {disk}% ---- {disk_result}\n\nOverall status: {serv}\n', exit_code
exit_code = 0
while True:
    if is_on == 2:
        break
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/home').percent
    res, exit_code = main(cpu, ram, disk)
    print(res)
    is_on = int(input('Хотите проверить еще раз?\n1. Да\n2. Нет\n'))
    if is_on == 2:
        break   
sys.exit(exit_code)




