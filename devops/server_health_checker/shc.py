print('Server Health Checker\n')
is_on = int(input('Начинаем?\n1. Да\n2. Нет\n'))

def cpu_check(cpu):
    if cpu < 80:
        return 'OK'
    elif 80<=cpu<=90:
        return 'WARNING'
    elif cpu > 90:
        return 'CRITICAL'

def ram_check(ram):
    if ram < 80:
        return 'OK'
    elif 80<=ram<=90:
        return 'WARNING'
    elif ram > 90:
        return 'CRITICAL'

def disk_check(disk):
    if disk < 90:
        return 'OK'
    elif 90<=disk<=95:
        return 'WARNING'
    elif disk > 95:
        return 'CRITICAL'

def service_status(service, cpu_result, ram_result, disk_result):
    if cpu_result == 'OK' and ram_result == 'OK' and disk_result == 'OK' and service == 1:
        return 'RUNNING'
    elif service == 2 or cpu_result == 'CRITICAL' or ram_result == 'CRITICAL' or disk_result == 'CRITICAL' :
        return 'CRITICAL'
    elif cpu_result == 'WARNING' or ram_result == 'WARNING' or disk_result == 'WARNING' :
        return 'WARNING'

while True:
    if is_on == 2:
        break
    cpu = int(input('Введите процент использования процессора:\n'))
    ram = int(input('Введите процент использования оперативной памяти:\n'))
    disk = int(input('Введите процент использования диска:\n'))
    service = int(input('Укажите статус сервиса:\n1. running\n2. stopped\n'))

    cpu_result = cpu_check(cpu)
    ram_result =  ram_check(ram)
    disk_result =  disk_check(disk)

    print(f'\n------------------------\nCPU: {cpu_result}\nRAM: {ram_result}\nDisk: {disk_result}\n\nServer status:{service_status(service, cpu_result, ram_result, disk_result)}\n------------------------\n')
    is_on = int(input('Еще раз проверить?\n1. Да\n2. Нет\n'))
    if is_on == 2:
        break


