import random

print('Это генератор паролей.\nОн генерирует случайный пароль из 12 знаков, включая цифры, буквы, символы.')
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ["!", '@', '#', '$']
ls = []
for i in range(0, 4):
    ls.append(random.choice(numbers))
    ls.append(random.choice(letters))
    ls.append(random.choice(symbols))

random.shuffle(ls)
print(*ls, sep='')