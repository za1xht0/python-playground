

print('Конвертер единиц измерения.\nОн конвертирует километры в мили, температуру из Цельсия в Фаренгейт, килограммы в фунты, сантиметры в дюймы и литры в галлоны.')

def km_to_miles(km):
    miles = km * 0.621371
    return miles

def temp_to_f(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

def kg_to_pounds(kg):
    pounds = kg * 2.20462
    return pounds

def cm_to_inches(cm):
    inches = cm * 0.393701
    return inches

def lit_to_gal(liters):
    gallons = liters * 0.264172
    return gallons

stop_word = ''
while stop_word != 'закончить':
    func = input('Выберите функцию конвертера:\n1 - Километры в мили\n2 - Цельсий в Фаренгейт\n3 - Килограммы в фунты\n4 - Сантиметры в дюймы\n5 - Литры в галлоны\n')
    if func == '1':
        km = float(input('Введите количество километров: '))
        print(f'{km} километров = {km_to_miles(km)} миль')
    elif func == '2':
        print('Введите температуру в Цельсиях:')
        celcius = float(input())
        print(f'{celcius}°C = {temp_to_f(celcius)}°F')
    elif func == '3':
        print('Введите количество килограммов:')
        kg = float(input())
        print(f'{kg} килограммов = {kg_to_pounds(kg)} фунтов')
    elif func == '4':
        print('Введите количество сантиметров:')
        cm = float(input())
        print(f'{cm} сантиметров = {cm_to_inches(cm)} дюймов')
    elif func == '5':
        print('Введите количество литров:')
        liters = float(input())
        print(f'{liters} литров = {lit_to_gal(liters)} галлонов')
    print('Если хочешь закончить, напиши - закончить\nЕсли продолжаем - напиши продолжаем\n')
    stop_word = input()