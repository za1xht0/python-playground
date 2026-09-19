# Configuration Validator

Консольная программа для проверки корректности конфигурационных параметров: hostname, IP-адреса, порта и среды запуска.

## Как запустить

```bash
cd conf_valid
python conf_valid.py
```

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
production
Configuration: VALID
```

Если данные введены некорректно, программа покажет список ошибок и результат `Configuration: INVALID`.

[Вернуться к корневому README](../README.md)
