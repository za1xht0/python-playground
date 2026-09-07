import random

print('Это генератор паролей.\nОн генерирует случайный пароль из 12 знаков, включая цифры, буквы, символы.')
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ["!", '@', '#', '$']
password = []
stop_word = ''
while stop_word != 'закончить':
    for i in range(0, 4):
        password.append(random.choice(numbers))
        password.append(random.choice(letters))
        password.append(random.choice(symbols))
    random.shuffle(password)
    print('Вот ваш пароль: ', *password, sep='')
    password = []
    stop_word = input('Если хочешь закончить, напиши - закончить\nЕсли продолжаем - напиши продолжаем\n')