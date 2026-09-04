import random

print('Игра "Угадай число".\nЯ загадал случайное число от 1 до 100, а тебе нужно отдагать его.\nУ тебя будет 10 попыток.\nЯ буду давать подсказки, если твой вариант будет меньше или больше загаданного числа.\nУдачи!')
number = random.randint(1, 100)
is_get = False
trying = ''
for i in range(10):
    trying = int(input('Напиши предположение:'))
    if trying < number:
        print('Загаданное число больше')
    elif trying > number:
        print('Загаданное число меньше')
    elif trying == number:
        is_get = True
        break
if is_get:
    print('Ты угадал число!')
else:
    print(f'Ты не смог угадать число...\nПравильный ответ - {number}')
    
    