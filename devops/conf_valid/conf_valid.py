import ipaddress

print('Configuration Validator')
errors = []

hostname = input('Введите hostname:\n')
ip = input('Введите ip:\n')
port = input('Введите порт:\n')
environment = input('Введите environment:\n')


def check_hostname(hostname):
    if hostname != '':
        return hostname
    else:
        errors.append('Hostname is missing')

def check_ip(ip):
    if ip == '':
        errors.append('IP is missing')
    else:
        try:
            ipaddress.ip_address(ip)
            return ip
        except ValueError:
            errors.append('IP is invalid')

def check_port(port):
    if port == '':
        errors.append('Port is missing')
    else:
        try:
            port = int(port)
            if 1 <= port <= 65535:
                return port
            else:
                errors.append('Port is invalid')
        except ValueError:
            errors.append('Port is invalid')
        
def check_environment(environment):
    if environment == '':
        errors.append('Environment is missing')
    elif environment in ['dev', 'stage', 'prod']:
        return environment
    else:
        errors.append('Environment is invalid')

check_hostname(hostname)
check_ip(ip)
check_port(port)
check_environment(environment)

errors_text = '\n- '.join(errors)
if errors:
    print(f'\nConfiguration: INVALID\n\nErrors:\n{errors_text}')
else:
    print('Configuration: VALID')

