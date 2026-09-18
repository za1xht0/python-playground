print('калькулятор')

def get_number(mes):
    while True:
        try:
            return int(input(mes))
        except ValueError:
            print('Нужно ввести число!')

def get_operation():
    while True:
        func = input('Выберите фукнцию:\n1. Сложить\n2. Вычесть\n3. Умножить\n4. Разделить\nВведите номер выбранной операции\n')
        if func in ('1', '2', '3', '4'):
            return func
        else:
            print('Нужно ввести корректный номер операции')

while True:
    numb = get_number('Введите первое число:')
    numb2 = get_number('Введите второе число:')
    func = get_operation()

    if func == '1':
        print(f'{numb} + {numb2} = {numb+numb2}')
    elif func == '2':
        print(f'{numb} - {numb2} = {numb-numb2}')
    elif func == '3':
        print(f'{numb} * {numb2} = {numb*numb2}')
    elif func == '4':
        if numb2 == 0:
            print('Деление на ноль не допускается')
        else:
            print(f'{numb} / {numb2} = {numb/numb2}')
    offon = input('Продолжаем? Напиши да или нет\n').strip().lower()
    if offon != 'да':
        break

