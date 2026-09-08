print('Простенький конвертер единиц измерения.\nОн конвертирует километры в мили, температуру из Цельсия в Фаренгейт, килограммы в фунты, сантиметры в дюймы и литры в галлоны.')


stop_word = ''
while stop_word != 'закончить':
    func = input('Выберите функцию конвертера:\n1 - Километры в мили\n2 - Цельсий в Фаренгейт\n3 - Килограммы в фунты\n4 - Сантиметры в дюймы\n5 - Литры в галлоны\n')
    if func == '1':
        print('Введите количество километров:')
        km = float(input())
        miles = km * 0.621371
        print(f'{km} километров = {miles} миль')
    elif func == '2':
        print('Введите температуру в Цельсиях:')
        celcius = float(input())
        fahrenheit = (celcius * 9/5) + 32
        print(f'{celcius}°C = {fahrenheit}°F')
    elif func == '3':
        print('Введите количество килограммов:')
        kg = float(input())
        pounds = kg * 2.20462
        print(f'{kg} килограммов = {pounds} фунтов')
    elif func == '4':
        print('Введите количество сантиметров:')
        cm = float(input())
        inches = cm * 0.393701
        print(f'{cm} сантиметров = {inches} дюймов')
    elif func == '5':
        print('Введите количество литров:')
        liters = float(input())
        gallons = liters * 0.264172
        print(f'{liters} литров = {gallons} галлонов')
    print('Если хочешь закончить, напиши - закончить\nЕсли продолжаем - напиши продолжаем\n')
    stop_word = input()