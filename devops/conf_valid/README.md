# Configuration Validator

Консольная программа для проверки корректности конфигурационных параметров: hostname, IP-адреса, порта и среды запуска.


## Что проверяет программа

- hostname не должен быть пустым;
- IP должен быть корректным IPv4 или IPv6 адресом;
- порт должен быть целым числом в диапазоне от 1 до 65535;
- environment должен быть одним из значений: `dev`, `stage`, `prod`.

Если хотя бы одно поле заполнено неверно, программа выводит список ошибок и результат `Configuration: INVALID`.

## Пример работы

```
Configuration Validator
Введите hostname:
example.com
Введите ip:
192.168.1.10
Введите порт:
8080
Введите environment:
prod
Configuration: VALID
```

## Пример ошибки

```text
Configuration Validator
Введите hostname:

Введите ip:
999.999.999.999
Введите порт:
70000
Введите environment:
test

Configuration: INVALID

Errors:
- IP is invalid
- Port is invalid
- Environment is invalid
```

[Вернуться к корневому README](../../README.md)
