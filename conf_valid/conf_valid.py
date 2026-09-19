print('Configuration Validator')
errors = []

hostname = input('Введите hostname:\n')
ip = input('Введите ip:\n')
port = int(input('Введите порт:\n'))
environment = input('Введите environment:\n')


def check_hostname(hostname):
    if hostname != '':
        return hostname
    else:
        errors.append('Hostname is missing')
        return 'Hostname is missing'

def check_ip(ip):
    if ip != '':
        return ip
    else:
        errors.append('IP is missing')
        return 'IP is missing'

def check_port(port):
    if 1<=port<=65535:
        return port
    else:
        errors.append('Port is invalid')
        return 'Port is invalid'

def check_environment(environment):
    if environment == 'production' or environment == 'staging' or environment == 'development':
        return 'OK'
    else:
        errors.append('Environment is invalid')
        return 'Error'

hostname_re = check_hostname(hostname)
ip_re = check_ip(ip)
port_re = check_port(port)
env_re = check_environment(environment)


if port_re == 'Port is invalid' or hostname_re == 'Hostname is missing' or ip_re == 'IP is missing' or env_re == 'Error':
    print(*errors, 'Configuration: INVALID', sep='\n')
else:
    print('Configuration: VALID')

