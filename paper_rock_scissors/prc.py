import random

print('Игра камень ножницы бумага')

choices = ['Камень', 'Ножницы', 'Бумага']
raw = ''
while raw not in ['1', '2', '3']:
    raw = input('Выберите:\n1. Камень\n2. Ножницы\n3. Бумага\n(Нужно ввести число)\n')
    try:
        player = int(raw)
        if player < 1 or player > 3:
            print('Нужно ввести число от 1 до 3')
            player = -1
    except ValueError:
        print('Нужно ввести число')
        player = -1

pl = choices[player - 1]
pc_answer = random.choice(choices)
print(pl, pc_answer)

if pl == 'Камень' and pc_answer == 'Бумага' or pl == 'Ножницы' and pc_answer == 'Камень' or pl == 'Бумага' and pc_answer == 'Ножницы':
    print("Ты проиграл")
elif pl == pc_answer:
    print('Ничья')
else:
    print("Ты выиграл")
