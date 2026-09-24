# Python Playground Launcher

CLI-лаунчер для запуска проектов из `python-playground` через единое терминальное меню.

## Возможности

* запуск Beginner и DevOps проектов;
* выбор проекта через CLI;
* возврат в меню после завершения проекта;
* обработка неправильного ввода;
* выход через `0`;
* запуск проектов через текущий Python-интерпретатор.

## Использование

Запуск из корня репозитория:

```bash
python launcher/main.py
```

После запуска появится список доступных проектов:

```text
[Beginner]

1. Calculator
2. Dice roll
3. Guess the number
...

[DevOps]

10. Server Health Checker
11. Configuration Validator
12. Server diff

0. Exit
```

Введите номер проекта для запуска или `0` для выхода.

## Технологии

* Python
* `subprocess`
* `sys`

