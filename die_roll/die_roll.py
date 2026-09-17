import random

print('Игра бросок кубика.\nПобеждает тот, кто первым наберет 3 победы. ')
is_win = False
count_pc = 0
count_player = 0


while is_win == False:
    player = random.randint(1, 6)
    pc = random.randint(1, 6)
    if player == pc:
        print('ничья')
    elif player > pc:
        count_player += 1
        print(f'ты победил в этом раунде. у тебя выпало {player}, у пк было {pc}\nСчетчик твоих побед: {count_player}\nСчетчик побед пк: {count_pc}')
    elif pc > player:
        count_pc += 1
        print(f'ты проиграл в этом раунде. у тебя выпало {player}, у пк было {pc}\nСчетчик твоих побед: {count_player}\nСчетчик побед пк: {count_pc}')
    if count_player == 3 or count_pc == 3:
        is_win = True
if count_player == 3:
    print('ты победил')
elif count_pc == 3:
    print('ты проиграл...')

    
