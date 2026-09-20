# Python Playground

Коллекция небольших Python-проектов для практики: от простых консольных
скриптов до работы с логикой и пользовательским вводом.

---

## Проекты

| Проект | Описание |
|---|---|
| [Guess the Number](./guess_number/README.md) | Игра «угадай число» |
| [Magic Ball](./magic_ball/README.md) | Аналог Magic 8-Ball — случайный ответ на вопрос |
| [Password Generator](./password_generator/README.md) | Генератор случайных паролей |
| [Unit Converter](./unit_converter/README.md) | Конвертер единиц измерения |
| [Paper-Rock-Scissors](./paper_rock_scissors/README.md) | Игра "камень-ножницы-бумага» |
| [Dice roll](./dice_roll/README.md) | Бросание кубика  |
| [Username generator](./username_generator/README.md) | Генератор никнеймов  |
| [Calculator](./calc/README.md) | Простой калькулятор  |
| [Server_Health_checker](./server_health_checker/README.md) | Программа проверки состояния  |

## Быстрый старт

```bash
git clone https://github.com/za1xht0/python-playground.git
cd python-playground
```

Каждый проект — самостоятельный скрипт, запускается отдельно:

```bash
python guess_number/guess.py
python magic_ball/magic.py
python password_generator/pass.py
python unit_converter/unit_con.py
```

## CI/CD

Используется GitHub Actions для автоматических проверок и деплоя.

Pipeline:

1. Получение кода из репозитория
2. Проверка HTML
3. Проверка ссылок
4. Проверка CSS
5. Деплой на GitHub Pages

## Website

https://za1xht0.github.io/python-playground/